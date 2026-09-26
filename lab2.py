def encrypt(message, key):
    cipher = ""

    for i in range(len(message)):
        p = ord(message[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        c = (p + k) % 26
        cipher += chr(c + ord('A'))

    return cipher


def decrypt(cipher, key):
    message = ""

    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        p = (c - k) % 26
        message += chr(p + ord('A'))

    return message


message = input("Enter message: ").upper()
key = input("Enter key: ").upper()

encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)