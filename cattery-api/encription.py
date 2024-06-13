""" 
Install the Cryptography Package: pip install cryptography
"""
from cryptography.fernet import Fernet

# # Generate a key
# key = Fernet.generate_key()

# with open('secret.key', 'wb') as key_file:
#     key_file.write(key)

with open('secret.key', 'rb') as key_file:
    key = key_file.read()
    
# Initialize Fernet with the generated key
fernet = Fernet(key)

credentials = "HOST=localhost\nPORT=8069\nDB=blog_tutorials\nUSER=admin\nPWD=admin"

# Encrypt the credentials
encrypted_credentials = fernet.encrypt(credentials.encode())

with open('credentials.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_credentials)

# Function to load and decrypt the environment variables
def load_credentials():
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open('credentials.enc', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted).decode().split('\n')

    return dict(line.split('=') for line in decrypted if line)

