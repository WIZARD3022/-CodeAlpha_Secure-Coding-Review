import subprocess
import os

def insecure_function():
    # Insecure: use of subprocess with shell=True
    subprocess.call('dir', shell=True)

def insecure_file_operation():
    # Insecure: use of eval for file operations
    file_path = 'text.txt'
    eval(f"open('{file_path}', 'w').write('Hello World')")

def insecure_os_system():
    # Insecure: use of os.system (adjusted to prevent data loss)
    os.system('echo This is a test command')

def insecure_cryptography():
    # Insecure: use of weak cryptographic method
    import hashlib
    hashlib.md5(b"some data").hexdigest()

def insecure_yaml_load():
    # Insecure: use of yaml.load() without Loader
    import yaml
    yaml_string = """
    foo: bar
    """
    data = yaml.load(yaml_string)
    print(data)

insecure_function()
insecure_file_operation()
insecure_os_system()
insecure_cryptography()
insecure_yaml_load()
