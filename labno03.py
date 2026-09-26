# Monoalphabetic Substitution Cipher
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
message = input("Enter message: ").upper()
# Encryption
encrypted = ""
for c in message:
    if c in alphabet:
        encrypted += key[alphabet.index(c)]
    else:
        encrypted += c
print("Encrypted:", encrypted)
# Decryption
decrypted = ""
for c in encrypted:
    if c in key:
        decrypted += alphabet[key.index(c)]
    else:
        decrypted += c
print("Decrypted:", decrypted)

