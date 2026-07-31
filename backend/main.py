from fastapi import FastAPI, UploadFile, File, Form, Header, HTTPException
from fastapi.responses import Response
from encryption.aes import encrypt, decrypt
from backend.ipfs import upload_to_ipfs
from backend.auth import create_token, verify_token
from backend.db import users, transactions, transfers
from hashing.sha256 import generate_hash
from blockchain.chain import calculate_block_hash
from pymongo.errors import DuplicateKeyError
from datetime import datetime
import requests

app = FastAPI()

users.create_index("username", unique=True)

# ---------------- HOME ---------------- #

@app.get("/")
def home():

    return {
        "message": "SecureChain Running"
    }

# ---------------- REGISTER ---------------- #

@app.post("/register")
def register(
    username: str = Form(...),
    password: str = Form(...)
):

    try:

        users.insert_one({
            "username": username,
            "password": password
        })

        return {
            "message": "User registered successfully"
        }

    except DuplicateKeyError:

        return {
            "message": "User already exists"
        }

# ---------------- LOGIN ---------------- #

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):

    user = users.find_one({
        "username": username,
        "password": password
    })

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token(username)

    return {
        "token": token
    }

# ---------------- VERIFY TOKEN ---------------- #

def get_user(token: str):

    try:

        data = verify_token(token)

        return data["user"]

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

# ---------------- UPLOAD ---------------- #

@app.post("/upload")
async def upload(
    file: UploadFile = File(...),
    token: str = Header(None)
):

    try:

        if not token:

            raise HTTPException(
                status_code=401,
                detail="Token missing"
            )

        user = get_user(token)

        data = await file.read()

        # HASH
        file_hash = generate_hash(data)

        # AES ENCRYPTION
        encrypted_data, key, nonce, tag = encrypt(data)

        # IPFS
        cid = upload_to_ipfs(
            encrypted_data,
            file.filename
        )

        # BLOCKCHAIN
        previous = transactions.find_one(
            sort=[("_id", -1)]
        )

        previous_hash = (
            previous.get("block_hash", "GENESIS")
            if previous else "GENESIS"
        )

        block = {

            "type": "UPLOAD",

            "user": user,

            "filename": file.filename,

            "hash": file_hash,

            "cid": cid,

            "key": key.hex(),

            "nonce": nonce.hex(),

            "tag": tag.hex(),

            "timestamp": str(datetime.now()),

            "previous_hash": previous_hash
        }

        block_hash = calculate_block_hash(block)

        block["block_hash"] = block_hash

        transactions.insert_one(block)

        return {

            "message": "Encrypted & stored in IPFS",

            "filename": file.filename,

            "hash": file_hash,

            "cid": cid,

            "key": key.hex(),

            "nonce": nonce.hex(),

            "tag": tag.hex(),

            "block_hash": block_hash
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ---------------- DOWNLOAD ---------------- #

@app.post("/download")
async def download(
    cid: str = Form(...),
    key: str = Form(...),
    nonce: str = Form(...),
    tag: str = Form(...),
    filename: str = Form(...),
    token: str = Header(None)
):

    try:

        user = get_user(token)

        res = requests.post(
            "http://127.0.0.1:5001/api/v0/cat",
            params={"arg": cid}
        )

        encrypted_data = res.content

        decrypted = decrypt(
            encrypted_data,
            bytes.fromhex(key),
            bytes.fromhex(nonce),
            bytes.fromhex(tag)
        )

        transactions.insert_one({

            "type": "DOWNLOAD",

            "user": user,

            "filename": filename,

            "cid": cid,

            "timestamp": str(datetime.now())
        })

        return Response(
            content=decrypted,
            media_type="application/octet-stream",
            headers={
                "Content-Disposition":
                f'attachment; filename="{filename}"'
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ---------------- TRANSFER FILE ---------------- #

@app.post("/transfer")
def transfer(
    receiver: str = Form(...),
    cid: str = Form(...),
    key: str = Form(...),
    nonce: str = Form(...),
    tag: str = Form(...),
    filename: str = Form(...),
    token: str = Header(None)
):

    try:

        sender = get_user(token)

        transfers.insert_one({

            "sender": sender,

            "receiver": receiver,

            "cid": cid,

            "key": key,

            "nonce": nonce,

            "tag": tag,

            "filename": filename,

            "timestamp": str(datetime.now())
        })

        transactions.insert_one({

            "type": "TRANSFER",

            "sender": sender,

            "receiver": receiver,

            "filename": filename,

            "cid": cid,

            "timestamp": str(datetime.now())
        })

        return {
            "message": "File transferred successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ---------------- USER FILES ---------------- #

@app.get("/files")
def get_files(
    token: str = Header(None)
):

    try:

        user = get_user(token)

        data = list(
            transactions.find(
                {
                    "user": user,
                    "type": "UPLOAD"
                },
                {
                    "_id": 0
                }
            )
        )

        return {
            "files": data
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ---------------- RECEIVED FILES ---------------- #

@app.get("/received")
def received_files(
    token: str = Header(None)
):

    try:

        receiver = get_user(token)

        data = list(

            transfers.find(

                {
                    "receiver": receiver
                },

                {
                    "_id": 0
                }
            )
        )

        return {
            "files": data
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ---------------- TRANSACTIONS ---------------- #

@app.get("/transactions")
def get_transactions(
    token: str = Header(None)
):

    try:

        user = get_user(token)

        data = list(
            transactions.find(
                {},
                {"_id": 0}
            )
        )

        return {
            "transactions": data
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )