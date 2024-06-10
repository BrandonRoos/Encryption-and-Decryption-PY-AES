from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet


# Generate a random key for encryption and decryption *key.key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Encrypt a mesage
def encrypt_message():
    try:
        key = open("key.key", "rb").read()
        fernet = Fernet(key)
        message = message_entry.get()
        encrypted_message = fernet.encrypt(message.encode())
        encrypted_entry.delete(0, END)
        encrypted_entry.insert(0, encrypted_message.decode())
    except Exception as e:
        messagebox.showerror("Error", "Encryption failed")

# Decrypt a message *key.key
def decrypt_message():
    try:
        key = open("key.key", "rb").read()
        fernet = Fernet(key)
        encrypted_message = encrypted_entry.get()
        decrypted_message = fernet.decrypt(encrypted_message.encode())
        decrypted_entry.delete(0, END)
        decrypted_entry.insert(0, decrypted_message.decode())
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed")

# Create the main screen
def main_screen():
    global message_entry, encrypted_entry, decrypted_entry

    root = Tk()
    root.title("Encryption and Decryption")

    label1 = Label(root, text="Enter a message:")
    message_entry = Entry(root, width=45)

    encrypt_button = Button(root, text="Encrypt", command=encrypt_message)

    label2 = Label(root, text="Encrypted message:")
    encrypted_entry = Entry(root, width=45)

    decrypt_button = Button(root, text="Decrypt", command=decrypt_message)

    label3 = Label(root, text="Decrypted message:")
    decrypted_entry = Entry(root, width=45)

    generate_key()

    label1.pack()
    message_entry.pack()
    encrypt_button.pack()
    label2.pack()
    encrypted_entry.pack()
    decrypt_button.pack()
    label3.pack()
    decrypted_entry.pack()

    root.mainloop()

if __name__ == "__main__":
    main_screen()