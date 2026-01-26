import string
from collections import Counter

class VigenereCipher:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.n = len(self.alphabet)
        
    def prepare_text(self, text):
        return ''.join(char.upper() for char in text if char.isalpha())
    
    def prepare_key(self, key, length):
        key = self.prepare_text(key)
        if not key:
            raise ValueError("Key must contain at least one letter")
        
        # Repeat key to match text length
        repeated_key = (key * (length // len(key) + 1))[:length]
        return repeated_key
    
    def encrypt(self, plaintext, key):
        plaintext = self.prepare_text(plaintext)
        key = self.prepare_key(key, len(plaintext))
        
        ciphertext = []
        for p_char, k_char in zip(plaintext, key):
            # Convert characters to numbers (A=0, B=1, ..., Z=25)
            p_num = self.alphabet.index(p_char)
            k_num = self.alphabet.index(k_char)
            
            # Vigenère encryption: C = (P + K) mod 26
            c_num = (p_num + k_num) % self.n
            ciphertext.append(self.alphabet[c_num])
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext, key):
        ciphertext = self.prepare_text(ciphertext)
        key = self.prepare_key(key, len(ciphertext))
        
        plaintext = []
        for c_char, k_char in zip(ciphertext, key):
            # Convert characters to numbers
            c_num = self.alphabet.index(c_char)
            k_num = self.alphabet.index(k_char)
            
            # Vigenère decryption: P = (C - K) mod 26
            p_num = (c_num - k_num) % self.n
            plaintext.append(self.alphabet[p_num])
        
        return ''.join(plaintext)
    
    def analyze_frequency(self, text):
        text = self.prepare_text(text)
        if not text:
            return {}
        
        counter = Counter(text)
        total = len(text)
        frequencies = {char: count/total * 100 for char, count in counter.items()}
        return frequencies
    

def main():
    cipher = VigenereCipher()
    
    print("=" * 50)
    print("VIGENÈRE CIPHER")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Analyze ciphertext")
        print("4. Show alphabet table")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            print("\n" + "-" * 30)
            plaintext = input("Enter plaintext: ")
            key = input("Enter key: ")
            
            encrypted = cipher.encrypt(plaintext, key)
            print(f"\nCiphertext: {encrypted}" + "\n" + "-" * 30)
            
        elif choice == '2':
            print("\n" + "-" * 30)
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            
            decrypted = cipher.decrypt(ciphertext, key)
            print(f"\nDecrypted: {decrypted}" + "\n" + "-" * 30)
            
        elif choice == '3':
            print("\n" + "-" * 30)
            text = input("Enter text to analyze: ")
            
            frequencies = cipher.analyze_frequency(text)
            print("\nLetter Frequencies (%):")
            for letter in sorted(frequencies.keys()):
                print(f"{letter}: {frequencies[letter]:.2f}%")

            print("-" * 30)
        
        elif choice == '4':
            print("\n" + "=" * 50)
            print("VIGENÈRE CIPHER TABULA RECTA")
            print("=" * 50)
            
            # Print table header
            header = "   " + " ".join(cipher.alphabet)
            print(header)
            print("-" * len(header))
            
            # Print table rows
            for i in range(26):
                row_letters = []
                for j in range(26):
                    row_letters.append(cipher.alphabet[(i + j) % 26])
                print(f"{cipher.alphabet[i]}: {' '.join(row_letters)}")
                
            print("-" * len(header))
        
        elif choice == '5':
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()