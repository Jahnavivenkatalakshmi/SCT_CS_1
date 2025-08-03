def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))

    if choice == 'E':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please select 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()
