from cryptography.fernet import Fernet  # Importing necessary module for encryption


def load_key():
    # Function to load the encryption key from a file
    with open("key.key", 'rb') as f:
        key = f.read()

    return key


key = load_key()  # Load the encryption key
fer = Fernet(key)  # Initialize the Fernet object for encryption and decryption


"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key) 
"""
# The above commented function is for generating a new encryption key and writing it to a file


def add():
    # Function to add a new username and password
    usr = input("Enter Username: ")
    pwd = input("Enter Password: ")

    # Append the encrypted username and password to the password.txt file
    with open("password.txt", 'a') as f:
        f.write(f"{usr}|{fer.encrypt(pwd.encode()).decode()} \n")


def view():
    # Function to view all stored usernames and passwords
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            # Decrypt and print each username and password
            print(f"User : {user} ,Password : {fer.decrypt(password.encode()).decode()}")


while True:
    # Main loop to ask user for actions
    action = input("What Do you want to do: (View, Add) or Press q to quit: ").lower()
    if action == "q":
        break
    if action == "view":
        view()  # If user wants to view passwords, call the view() function
    if action == "add":
        add()   # If user wants to add passwords, call the add() function
