from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key = input("Enter key: ").encode()
message = input("Enter message: ").encode()
# Encryption
cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(message, 8))
print("Encrypted:", encrypted.hex())
# Decryption
cipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted:", decrypted.decode())
