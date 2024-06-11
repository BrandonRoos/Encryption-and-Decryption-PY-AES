# Encryption and Decryption GUI

This project is a simple GUI application for encrypting and decrypting messages using the `cryptography` library and the `Fernet` symmetric encryption method. The GUI is built using `tkinter`, a standard Python interface to the Tk GUI toolkit.
<div>
<img src="https://img.shields.io/badge/-Python%20Cryptography-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  
</div>
## Features

- Generate a random key for encryption and decryption.
- Encrypt messages entered by the user.
- Decrypt encrypted messages.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- The `cryptography` library installed. You can install it using pip:
- The `tkinter` library installed for creating the graphical user interface (GUI). Tkinter is Python's standard GUI toolkit and is necessary to build and display the windowed interface for this application.

```bash
pip install tkinter
pip install cryptography
```

## Working GUI 
![Screenshot of gui](https://github.com/BrandonRoos/Encryption-and-Decryption-PY-AES/assets/28285286/cf699e80-c8ae-4c33-81bf-b603be465d47)

## Code Structure
The program consists of several functions that serve specific purposes:

- `generate_key`: This function generates a random key for encryption and decryption and saves it in a file called key.key.
- `encrypt_message`: This function reads the encryption key from key.key, uses it to create a Fernet cipher, encrypts the input message using AES encryption, and displays the encrypted message in the GUI.
- `decrypt_message`: This function reads the encryption key from key.key, uses it to create a Fernet cipher, decrypts the input encrypted message, and displays the decrypted message in the GUI.
- `main_screen`: This function creates the main GUI window using tkinter. It includes text entry fields for the original message, the encrypted message, and the decrypted message, along with buttons for encryption and decryption. The generate_key function is called to create the encryption key at the start.

## How to Use
Follow these steps to use the program:
1. Run the Program: Run the Python script, and a GUI window will appear.
2. Enter a Message: In the "Enter a message" field, type the message you want to encrypt.
3. Encryption: Click the "Encrypt" button to encrypt the message. The encrypted message will appear in the "Encrypted message" field.
4. Decryption: To decrypt the message, click the "Decrypt" button. The decrypted message will appear in the "Decrypted message" field.
5. Key Generation: The program generates an encryption key (key.key) automatically at the start. This key is used for both encryption and decryption. You don't need to manage the key; it's handled by the program.
6. Copy to Clipboard (Optional): You can copy the decrypted message to your clipboard by selecting and copying it from the "Decrypted message" field.
7. Handling Errors: If there are any errors during encryption or decryption, an error message will be displayed in a pop-up window.


## Customization
This code provides a basic example of AES encryption and decryption using tkinter. You can customize and enhance it further according to your specific requirements, such as implementing more secure key management practices or adding additional features to the GUI.

**Please note**: This code is for educational purposes and my portfolio. For real-world applications, you should consider additional security measures and key management practices. I will add more security measures in later versions. This code is a living document. Also, note this will be the first real code I am publishing on GitHub. Hello, World! and thank you for reading.



  



