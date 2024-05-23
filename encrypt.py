import gnupg
import os

# Initialize GPG
gpg = gnupg.GPG()

# Set paths for files
input_file = 'password.txt'
encrypted_file = 'password.txt.gpg'

def encrypt_file(input_file, output_file, recipient):
    with open(input_file, 'rb') as f:
        status = gpg.encrypt_file(f, recipients=[recipient], output=output_file)
        return status.ok

if __name__ == "__main__":
    # Replace this with the actual recipient's email or key ID
    recipient = 'fredredev@gmail.com'
    
    # Encrypt the file
    if encrypt_file(input_file, encrypted_file, recipient):
        print(f"File encrypted successfully to {encrypted_file}")
        os.remove(input_file)  # Delete the original file
        print(f"Original file {input_file} deleted")
    else:
        print("Encryption failed")

