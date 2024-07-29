import subprocess  # nosec
import os
import hashlib
import yaml
import platform

def secure_function():
    # Secure: use of subprocess without shell=True and with appropriate command
    if platform.system() == "Windows":
        subprocess.call(["cmd.exe", "/c", "dir"])  # nosec
    else:
        subprocess.call(['/bin/ls'])  # nosec

def secure_file_operation():
    # Secure: using proper file handling without eval
    file_path = 'text.txt'  # Relative path to the file
    with open(file_path, 'w') as f:
        f.write('Hello World')

def secure_os_system():
    # Secure: avoiding os.system for critical operations
    print("Simulating secure file deletion")

def secure_cryptography():
    # Secure: use of a secure cryptographic method
    hashlib.sha256(b"some data").hexdigest()

def secure_yaml_load():
    # Secure: use yaml.safe_load() instead of yaml.load()
    yaml_string = """
    foo: bar
    """
    data = yaml.safe_load(yaml_string)

secure_function()
secure_file_operation()
secure_os_system()
secure_cryptography()
secure_yaml_load()
