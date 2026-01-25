
# Encrypt text using Caesar cipher with given shift
def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a') # Determine ASCII start based on case
            shifted = (ord(char) - start + shift) % 26 # Shift character 
            result += chr(start + shifted)
        else:
            result += char # Keep non-alphabetic characters unchanged
    
    return result


def main():
    print("=" * 50)
    print("          Caesar Cipher Program")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypted = encrypt(message, shift)
            print(f"\nOriginal:  {message}")
            print(f"Encrypted: {encrypted}")
            
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            decrypted = encrypt(message, -shift) # Decrypting by reversing the shift
            print(f"\nEncrypted: {message}")
            print(f"Decrypted: {decrypted}")
            
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()