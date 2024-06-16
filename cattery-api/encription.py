""" 
Python script to encrypt and decrypt server details.
Requirement: pip install cryptography
"""
from cryptography.fernet import Fernet

# # Generate a key
# key = Fernet.generate_key()

# with open('secret.key', 'wb') as key_file:
#     key_file.write(key)

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()
    
# Initialize Fernet with the generated key
fernet = Fernet(key)

credentials = "HOST=localhost\nPORT=8069\nDB=blog_tutorials\nUSER=admin\nPWD=admin"

# Encrypt the credentials
encrypted_credentials = fernet.encrypt(credentials.encode())

with open('credentials.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_credentials)



