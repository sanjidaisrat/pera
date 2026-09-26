# ElGamal Encryption and Decryption
p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))
# Private key
x = int(input("Enter private key x: "))
# Public key
y = pow(g, x, p)
# Message
message = int(input("Enter message: "))
# Random key
k = int(input("Enter random key k: "))
# Encryption
c1 = pow(g, k, p)
c2 = (message * pow(y, k, p)) % p
print("Public key:", y)
print("Ciphertext:", c1, c2)
# Decryption
s = pow(c1, x, p)
s_inverse = pow(s, -1, p)
decrypted = (c2 * s_inverse) % p
print("Decrypted message:", decrypted)