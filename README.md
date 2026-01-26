# Cyber-Projects

An educational repository containing beginner to intermediate Python scripts spanning cybersecurity domains including cryptography, network security, defensive tools, offensive security utilities, and hands-on automation practice. This collection demonstrates practical implementations of security tools and concepts using Python.

**Disclaimer: These tools are for educational purposes, authorized testing, and skill development only. Unauthorized access to systems without permission is illegal.**

## Projects Overview

### 1. [Port Scanner](Port%20Scanner)

A multi-threaded TCP port scanner that identifies open and closed ports on target hosts.

**Features:**
- Fast parallel scanning using 50 concurrent threads
- Scans common ports 1-1024
- Supports both IP addresses and hostname resolution
- Thread-safe output with clean result display
- Sorted results for easy analysis

**Key Technologies**: `socket`, `threading`, `Queue`

---
### 2. [Caesar Cipher](Caesar%20Cipher)

A simple implementation of the Caesar cipher algorithm for encrypting and decrypting text messages.

**Features:**
- Encrypt messages with a specified shift value
- Decrypt messages by reversing the shift
- Case preservation for uppercase and lowercase letters
- Non-alphabetic character preservation (numbers, spaces, special characters)
- Interactive command-line menu interface

**Key Technologies**: String manipulation, ASCII encoding, modulo arithmetic 

---
### 3. [Vigenère Cipher](Vigenère%20Cipher)

An advanced polyalphabetic cipher that uses multiple substitution alphabets based on a keyword.

**Features:**
- Polyalphabetic encryption/decryption with key management
- Letter frequency analysis for cryptanalysis
- Interactive CLI with Tabula Recta display
- Automatic text cleaning and case handling

**Key Technologies:** Polyalphabetic substitution, frequency analysis, modular arithmetic

---
### 4. [SMTP Mailer](SMTP%20Mailer)

An email utility for sending messages programmatically using SMTP protocol.

**Key Technologies**: `smtplib`, Email protocols

#### Requirements

- Python 3.x
- Standard library modules (no external dependencies for most scripts)

---
### 5. [Simple DoS Script](Simple%20DoS%20Script)

An educational Denial of Service attack script demonstrating network attack concepts.

**Note**: This tool is strictly for educational purposes and authorized testing only. Unauthorized DoS attacks are illegal.

**Key Technologies**: Network protocols, attack simulation


## Educational Purpose

These scripts are designed to:
- Demonstrate cybersecurity concepts
- Teach network programming in Python
- Practice threading and concurrent programming
- Understand security tools and their implementation
- Learn about ethical hacking practices

## Contributing

This is an educational project. Feel free to:
- Fork and improve the scripts
- Add more cybersecurity tools
- Enhance documentation
- Fix bugs or optimize performance

## Disclaimer

These tools are provided for educational and authorized security testing purposes only. The author is not responsible for misuse or illegal activities. Always follow applicable laws and regulations.


**⚠️ Legal Disclaimer:**
- Use these tools only on systems you own or have explicit permission to test
- Unauthorized access to computer systems violates laws in most jurisdictions
- Unauthorized DoS attacks are illegal
- Unauthorized port scanning may violate network usage policies
- Always obtain written permission before testing any system

## License

See LICENSE file for details.