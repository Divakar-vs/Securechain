# Securechain
Developed a blockchain-enabled secure file storage and transfer system using FastAPI, Streamlit, MongoDB, and IPFS, implementing AES-256-GCM encryption, SHA-256 hashing, and JWT authentication for secure file management. 
# SecureChain – Secure File Storage and Transfer Using Blockchain & IPFS

## Overview

SecureChain is a secure file storage and transfer application that combines **Blockchain**, **IPFS (InterPlanetary File System)**, and **AES-256 encryption** to provide secure, decentralized, and tamper-resistant file sharing.

Instead of storing files directly on a centralized server, SecureChain encrypts files, uploads the encrypted data to IPFS, and stores the file metadata and integrity information in a blockchain-based transaction ledger.

---

# Features

* User Registration and Login
* JWT Authentication
* AES-256 File Encryption
* Secure File Upload
* IPFS Distributed Storage
* SHA-256 File Integrity Verification
* Blockchain Transaction Logging
* Secure File Download
* File Transfer Between Users
* MongoDB Database Integration
* FastAPI Backend
* Streamlit Frontend

---

# Technology Stack

## Frontend

* Streamlit
* HTML/CSS (Streamlit Components)

## Backend

* FastAPI
* Python

## Database

* MongoDB

## Blockchain

* Custom Blockchain Ledger

## Storage

* IPFS (Kubo)

## Encryption

* AES-256 GCM
* SHA-256 Hashing

---

# Project Structure

```text
SecureChain/
│
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── db.py
│   ├── ipfs.py
│   └── blockchain/
│       └── chain.py
│
├── encryption/
│   └── aes.py
│
├── hashing/
│   └── sha256.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# System Architecture

```text
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ├──────── Encrypt File (AES-256)
   │
   ├──────── Generate SHA-256 Hash
   │
   ├──────── Upload Encrypted File to IPFS
   │
   ├──────── Store Metadata in MongoDB
   │
   └──────── Record Blockchain Transaction
```

---

# Prerequisites

Install the following software before running the project.

* Python 3.10 or later
* Git
* MongoDB Community Server
* IPFS Kubo
* Streamlit
* FastAPI

---

# Step 1 – Clone the Repository

```bash
git clone https://github.com/<your-username>/SecureChain.git

cd SecureChain
```

---

# Step 2 – Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

Command Prompt

```bash
.venv\Scripts\activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

# Step 3 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 – Install MongoDB

Start MongoDB.

```bash
mongod
```

Open another terminal.

```bash
mongosh
```

---

# Step 5 – Install IPFS

Download and install IPFS Kubo.

Initialize IPFS.

```bash
ipfs init
```

Start the daemon.

```bash
ipfs daemon
```

Wait until you see:

```text
Daemon is ready
```

---

# Step 6 – Configure Environment Variables

Create a file named `.env`.

Example:

```env
MONGO_URI=mongodb://localhost:27017
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Step 7 – Run the Backend

```bash
uvicorn backend.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

The FastAPI Swagger interface should load.

---

# Step 8 – Run the Frontend

Open a new terminal.

```bash
streamlit run frontend/app.py
```

The application opens in your browser.

---

# Step 9 – Register

Create a new account.

Example

```
Username: demo
Password: demo123
```

---

# Step 10 – Login

Login using your credentials.

A JWT access token is generated for authenticated requests.

---

# Step 11 – Upload a File

Choose a file.

During upload SecureChain:

1. Reads the file.
2. Generates a SHA-256 hash.
3. Encrypts the file using AES-256 GCM.
4. Uploads the encrypted file to IPFS.
5. Receives an IPFS CID.
6. Stores metadata in MongoDB.
7. Records the transaction in the blockchain ledger.

The upload response includes:

* Filename
* File Hash
* CID
* Block Hash
* Previous Hash

---

# Step 12 – Download a File

Provide:

* CID
* Encryption Key
* Nonce
* Authentication Tag

The system:

1. Downloads encrypted data from IPFS.
2. Decrypts the file.
3. Verifies the SHA-256 hash.
4. Returns the original file.

---

# Step 13 – Transfer a File

Enter:

* Receiver
* CID
* Encryption Key
* Nonce
* Tag

A blockchain transaction is recorded.

---

# API Endpoints

| Method | Endpoint        | Description                         |
| ------ | --------------- | ----------------------------------- |
| POST   | `/register`     | Register a user                     |
| POST   | `/login`        | Login and receive a JWT             |
| POST   | `/upload`       | Upload an encrypted file            |
| POST   | `/download`     | Download and decrypt a file         |
| POST   | `/transfer`     | Transfer a file                     |
| GET    | `/transactions` | View blockchain transaction history |

---

# Database Collections

## Users

```text
username
password
```

## Transactions

```text
type
user
filename
hash
cid
timestamp
previous_hash
block_hash
```

## Transfers

```text
sender
receiver
filename
cid
timestamp
```

---

# Security Features

* AES-256 GCM Encryption
* SHA-256 Integrity Verification
* JWT Authentication
* Blockchain Audit Trail
* IPFS Distributed Storage
* Tamper Detection

---

# Future Enhancements

* Smart Contract Integration
* MetaMask Authentication
* Role-Based Access Control
* AI-Based Threat Detection
* File Versioning
* Multi-Factor Authentication
* Email Notifications
* Cloud Deployment
* Docker Support

---

# Screenshots

Add screenshots for:

* Login Page
* Dashboard
* Upload Screen
* Download Screen
* Blockchain Transactions
* MongoDB Collections
* FastAPI Swagger UI

---

# Author

**Divakar V S**

MCA (Cybersecurity)

Python Developer | Blockchain Enthusiast | AI & Secure Software Development

GitHub: https://github.com/Divakar-vs
