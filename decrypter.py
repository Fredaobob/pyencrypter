import gnupg
import os
import getpass

# Initialize GPG
gpg = gnupg.GPG()

# Set paths for files
encrypted_file = 'password.txt.gpg'
decrypted_file = 'password.txt'

def decrypt_file(input_file, output_file, passphrase):
    with open(input_file, 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=passphrase, output=output_file)
        print(f"Status: {status.status}")
        print(f"Stderr: {status.stderr}")
        return status.ok

if __name__ == "__main__":
    # Prompt for the passphrase
    passphrase = getpass.getpass(prompt='Enter your GPG passphrase: ')
    
    # Decrypt the file
    if decrypt_file(encrypted_file, decrypted_file, passphrase):
        print(f"File decrypted successfully to {decrypted_file}")
        os.remove(encrypted_file)  # Delete the encrypted file
        print(f"Encrypted file {encrypted_file} deleted")
    else:
        print("Decryption failed")

