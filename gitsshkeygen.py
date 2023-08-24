import os
import subprocess

# Get GitHub email
email = input("Please enter your GitHub email: ")

# Ask for passphrase
use_passphrase = input("Do you want to set a passphrase? (yes/no): ").lower() == 'yes'
passphrase = ''
if use_passphrase:
    passphrase = input("Please enter your passphrase: ")

# Get file name for the key, with a default value
file_name = input("Enter the name of the file (default is id_rsa): ")
if file_name == '':
    file_name = "id_rsa"

# Define the path to the .ssh directory
ssh_path = os.path.expanduser(f'~/.ssh/{file_name}')

# Generate SSH key
subprocess.run(f'ssh-keygen -t rsa -b 4096 -C "{email}" -f "{ssh_path}" -N "{passphrase}"', shell=True)

# Add the key using ssh-add
subprocess.run(f'ssh-add {ssh_path}', shell=True)

# Print the public key
with open(f'{ssh_path}.pub', 'r') as file:
    public_key = file.read().strip()
    print("\nYour public key is:")
    print(public_key)
    print("Please enter this into your GitHub settings.")
