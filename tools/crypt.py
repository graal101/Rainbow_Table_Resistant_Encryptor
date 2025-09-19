from cryptography.fernet import Fernet
import base64
import hashlib
import os

def generate_key(password: str) -> bytes:
    """Генерирует ключ на основе пароля."""
    # Хешируем пароль с использованием SHA-256
    password_bytes = password.encode()
    # Генерируем ключ длиной 32 байта
    key = hashlib.pbkdf2_hmac('sha256', password_bytes, os.urandom(16), 100000)
    return base64.urlsafe_b64encode(key)


def encrypt_string(password: str, plaintext: str) -> str:
    """Шифрует строку с использованием пароля."""
    key = generate_key(password)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    return encrypted.decode()

def decrypt_string(password: str, encrypted_text: str) -> str:
    """Дешифрует строку с использованием пароля."""
    key = generate_key(password)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_text.encode())
    return decrypted.decode()
