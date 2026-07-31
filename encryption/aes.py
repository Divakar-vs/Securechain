from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(data):

    key = get_random_bytes(32)

    cipher = AES.new(key, AES.MODE_GCM)

    encrypted_data, tag = cipher.encrypt_and_digest(data)

    return encrypted_data, key, cipher.nonce, tag


def decrypt(data, key, nonce, tag):

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    return cipher.decrypt_and_verify(data, tag)