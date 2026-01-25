# Caesar Cipher

A simple implementation of the Caesar cipher algorithm for encrypting and decrypting text messages.

## Description

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. This program allows users to encrypt messages with a specified shift value and decrypt messages by reversing the shift.

## Features

- **Encrypt messages**: Shift characters by a specified amount
- **Decrypt messages**: Reverse the encryption using the same shift value
- **Case preservation**: Maintains uppercase and lowercase letters
- **Non-alphabetic preservation**: Keeps numbers, spaces, and special characters unchanged
- **Interactive menu**: User-friendly command-line interface

## Usage

Run the program:
```bash
python caesar_cipher.py
```

Then select an option:
1. Encrypt a message - Enter your message and shift value
2. Decrypt a message - Enter the encrypted message and shift value
3. Exit - Close the program

### Example

```
Original:  Hello World
Encrypted: Khoor Zruog (with shift of 3)
```

## Requirements

- Python 3.x

## Author

Created as a cybersecurity project example.
