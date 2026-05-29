# Encryption and Decryption GUI

A simple GUI application for encrypting and decrypting messages using the `cryptography` library's `Fernet` recipe. Fernet provides authenticated symmetric encryption built on **AES-128 in CBC mode** with an **HMAC-SHA256** signature for integrity, so altered ciphertext fails to decrypt rather than returning corrupted data. The interface is built with `tkinter`, Python's standard GUI toolkit.

<div>
<img src="https://img.shields.io/badge/-Python%20Cryptography-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</div>

## Features

- Generates an encryption key at runtime (kept local, never committed to the repo).
- Encrypts messages entered by the user.
- Decrypts encrypted messages.
- Verifies integrity automatically via Fernet's built-in HMAC.

## A Note on Fernet vs. "raw" AES

Fernet is a higher-level wrapper around AES rather than a bare implementation, and that's intentional — it bundles a secure mode (CBC), random IV generation, and message authentication together, avoiding the classic mistakes of hand-rolled AES (reused IVs, missing integrity checks, ECB mode). If raw AES with manual mode selection is ever needed, the `cryptography` library's `Cipher` API supports that directly.

## Prerequisites

- Python 3.x installed on your machine.
- The `cryptography` library, installed with pip:

```bash
pip install cryptography
```

Tkinter is Python's standard GUI toolkit and ships with most Python installations, so it usually does not need to be installed separately. (On some Linux distributions it's available through the system package manager, e.g. `sudo apt install python3-tk`.)

## Working GUI

![Screenshot of gui](https://github.com/BrandonRoos/Encryption-and-Decryption-PY-AES/assets/28285286/cf699e80-c8ae-4c33-81bf-b603be465d47)

## Code Structure

The program is organized into a few focused functions:

- `generate_key`: Generates a Fernet key at runtime and saves it locally to `key.key`. This file is git-ignored and should never be committed.
- `encrypt_message`: Loads the key, creates a Fernet cipher, encrypts the input message, and displays the ciphertext in the GUI.
- `decrypt_message`: Loads the key, decrypts the ciphertext, and displays the result — automatically failing if integrity verification fails.
- `main_screen`: Builds the main tkinter window with entry fields for the original, encrypted, and decrypted messages plus the encrypt/decrypt controls. `generate_key` is called at startup.

## How to Use

1. **Run the program:** Launch the Python script and the GUI window appears.
2. **Enter a message:** Type your message in the "Enter a message" field.
3. **Encrypt:** Click "Encrypt" — the ciphertext appears in the "Encrypted message" field.
4. **Decrypt:** Click "Decrypt" — the original text appears in the "Decrypted message" field.
5. **Key generation:** A key (`key.key`) is generated automatically at startup and used for both operations; you don't need to manage it manually.
6. **Copy to clipboard (optional):** Select and copy the result from the message field.
7. **Error handling:** Any errors during encryption or decryption surface in a pop-up dialog.

## Security Notes

- **Key handling.** The key lives in `key.key`, generated locally and excluded via `.gitignore`. Anyone with the key can decrypt the data, so a real deployment should store it in a secrets manager or OS keychain rather than a flat file — never commit it to a repository.
- **Scope.** This is a learning and portfolio project demonstrating applied symmetric cryptography. Production use would add key rotation, key derivation (e.g., PBKDF2 or Argon2 from a user password), and secure key storage.

## Possible Improvements

- Password-derived keys via a KDF so users aren't managing a raw key file.
- File encryption in addition to text.
- Key rotation support.


  



