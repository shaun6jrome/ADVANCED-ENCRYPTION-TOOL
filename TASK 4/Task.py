import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding

backend = default_backend()


def derive_key(password: str, salt: bytes, iterations: int = 100000) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=backend
    )
    return kdf.derive(password.encode())


def encrypt_file(file_path: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    with open(file_path, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f'✅ File encrypted: {file_path}.enc')


def decrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = data[:16]
    iv = data[16:32]
    encrypted_data = data[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    original_path = file_path.replace('.enc', '.dec')
    with open(original_path, 'wb') as f:
        f.write(data)

    print(f'✅ File decrypted: {original_path}')


if __name__ == '__main__':
    print("🔐 AES-256 File Encryptor/Decryptor")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Choose an option (1/2): ")

    path = input("Enter file path: ")
    pwd = input("Enter password: ")

    if choice == '1':
        encrypt_file(path, pwd)
    elif choice == '2':
        decrypt_file(path, pwd)
    else:
        print("❌ Invalid choice")

