import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = b"Kritiks_Strongest_password"
salt = os.urandom(16)
iterations = 100000
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256(),
  length=32,
  salt=salt,
  iterations=iterations
)
key = base64.urlsafe_b64encode(kdf.derive(password))
fernet = Fernet(key)
file_to_encrypt = "my_file.txt"
with open(file_to_encrypt, "rb") as f:
  file_data = f.read()
encrypted_data = fernet.encrypt(file_data)
with open(file_to_encrypt + ".encrypted", "wb") as f:
  f.write(encrypted_data)
file_to_decrypt = file_to_encrypt + ".encrypted"
with open(file_to_decrypt, "rb") as f:
  encrypted_data = f.read()
decrypted_data = fernet.decrypt(encrypted_data)
with open(file_to_decrypt + ".decrypted", "wb") as f:
  f.write(decrypted_data)
