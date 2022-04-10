from posixpath import split
from cryptography.fernet import Fernet


master_pwd = input("Enter master password? ")
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user,"Password:", fer.decrypt(passw.encode()).decode()   )

def add():
    name = input("Account Name: ")
    pwd = input("Enter Password: ")

    #with open means it will open a file and close by itself no need to f.close() 
    # "a" means append to a file and also it will create a file if not exist
    
    with open("password.txt", "a") as f:
        f.write(name +"|" + fer.encrypt(pwd.encode()).decode()  + "\n")



while True:
    mode = input("Would you like to add new password or view existing ones (view, add) or press q to quit? ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
        continue
    elif mode == "add":
        add()
        continue
    else:
        print("Invalid mode!!!! Please enter add or view only.")
        continue
