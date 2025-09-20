from cryptography.fernet import Fernet
import base64
import hashlib
import os

def generate_key(password: str, salt: bytes) -> bytes:
    """Генерирует ключ на основе пароля и соли."""
    password_bytes = password.encode()
    # Генерируем ключ длиной 32 байта
    key = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    return base64.urlsafe_b64encode(key)

def encrypt_string(password: str, plaintext: str) -> str:
    """Шифрует строку с использованием пароля."""
    # Генерируем соль
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    # Сохраняем соль и зашифрованные данные вместе
    return base64.urlsafe_b64encode(salt + b':' + encrypted).decode()

def decrypt_string(password: str, encrypted_text: str) -> str:
    """Дешифрует строку с использованием пароля."""
    # Декодируем зашифрованные данные
    decoded_data = base64.urlsafe_b64decode(encrypted_text.encode())
    # Извлекаем соль и зашифрованные данные
    salt = decoded_data[:16]
    encrypted_data = decoded_data[16:]
    
    key = generate_key(password, salt)
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_data)
        return decrypted.decode()
    except Exception as e:
        print(f"Ошибка при расшифровке: {e}")
        return None
