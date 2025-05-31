from cryptography.fernet import Fernet

# Load your encryption key
with open("encryption.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Password to encrypt
password = "Archery673412"

encrypted_pass = cipher.encrypt(password.encode())

print(encrypted_pass.decode()) 
