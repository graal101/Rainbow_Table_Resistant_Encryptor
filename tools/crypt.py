import base64
import hashlib
import os
import re
from cryptography.fernet import Fernet

class Crypt():
    def __init__(self, passw: str, plain_text: str, Nchar: int = 14):
        self.__passw = passw
        self.__plain_text = plain_text
        self.__Nchar = Nchar
        
    def val_length(self) -> bool:
        """Проверка длины пароля."""
        print(self.__Nchar)
        if len(self.__passw) < self.__Nchar:
            return False
        return True
        
    def val_special_char(self) -> bool:
        """Проверка наличия спец символов"""
        # Регулярное выражение для спецсимволов
        has_special_char = re.compile(r'[!_@#$%^&*(),.?":{}|<>]')
        if not has_special_char.search(self.__passw):
            return False
        return True
        

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
        print(f'Ошибка при расшифровке: {e}')
        return None
