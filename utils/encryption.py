from cryptography.fernet import Fernet


def encrypt_id(user_id: str, key: str) -> str:
    f = Fernet(key)
    token = f.encrypt(user_id.encode("utf-8"))
    return token.decode("utf-8")


def decrypt_id(token: str, key: str) -> str:
    f = Fernet(key)
    plaintext = f.decrypt(token.encode("utf-8"))
    return plaintext.decode("utf-8")
