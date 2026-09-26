def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
# Input
message = input("Enter message: ")
shift = int(input("Enter shift value: "))
# Encryption
encrypted = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted)
# Decryption
decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted message:", decrypted)


