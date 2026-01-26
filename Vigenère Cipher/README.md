# Vigenère Cipher Implementation

A clean, educational Python implementation of the Vigenère cipher with an interactive command-line interface.

## Features

- **Full Vigenère Cipher Implementation**: Authentic encryption and decryption
- **Interactive CLI**: User-friendly menu-driven interface
- **Text Analysis**: Letter frequency analysis for cryptanalysis practice
- **Tabula Recta Display**: Visual representation of the Vigenère square
- **Automatic Text Cleaning**: Handles non-alphabetic characters gracefully

## Installation

1. Ensure you have Python 3.6+ installed:
   ```bash
   python --version
   ```

2. No external dependencies required! This uses only Python's standard library.

## Usage

Run the program:
```bash
python vigenere_cipher.py
```

### Menu Options

1. **Encrypt message**: Convert plaintext to ciphertext using a keyword
2. **Decrypt message**: Convert ciphertext back to plaintext using the same keyword
3. **Analyze ciphertext**: View letter frequency distribution (helpful for cryptanalysis)
4. **Show alphabet table**: Display the complete Vigenère square (Tabula Recta)
5. **Exit**: Close the program

## How It Works

### The Vigenère Cipher
The Vigenère cipher is a **polyalphabetic substitution cipher** that uses multiple Caesar ciphers based on a keyword. This makes it much more secure than simple substitution ciphers.

**Encryption Formula**: `Cᵢ = (Pᵢ + Kᵢ) mod 26`
**Decryption Formula**: `Pᵢ = (Cᵢ - Kᵢ) mod 26`

Where:
- `Pᵢ` = Plaintext letter (converted to number A=0, B=1, ..., Z=25)
- `Kᵢ` = Key letter (converted similarly)
- `Cᵢ` = Ciphertext letter

### Example

```
Plaintext:  ATTACKATDAWN
Key:        LEMONLEMONLE
Ciphertext: LXFOPVEFRNHR
```

## Security Note

**This is for educational purposes only!** The Vigenère cipher was broken in the 19th century and provides **no real security** against modern attacks. Do not use this for securing sensitive information.

## Testing Examples

### Example: 
```
Plaintext:  TOBEORNOTTOBETHATISTHEQUESTION
Key:        HAMLET
Ciphertext: AOWZWLOBNEMWLRAMEAWLAAWWUMUXN
```

## Cryptanalysis

The Vigenère cipher can be broken by:
1. Determining key length using Kasiski examination or Index of Coincidence
2. Treating each column as a Caesar cipher
3. Using frequency analysis on each column

## Project Structure

```
vigenere_cipher.py
├── VigenereCipher class
│   ├── encrypt(plaintext, key)
│   ├── decrypt(ciphertext, key)
│   ├── prepare_text(text)
│   ├── prepare_key(key, length)
│   └── analyze_frequency(text)
└── main() - Interactive CLI
```


---

*"The Vigenère cipher is not secure, but it's a beautiful introduction to polyalphabetic cryptography."*

## 🔗 Related Resources

- [Cryptography I - Stanford University (Coursera)](https://www.coursera.org/learn/crypto)
- [The Code Book by Simon Singh](https://simonsingh.net/books/the-code-book/)
- [CryptoHack - Interactive cryptography challenges](https://cryptohack.org/)