from math import gcd
p = int(input("Enter p: "))
q = int(input("Enter q: "))
n = p * q
phi = (p - 1) * (q - 1)
e = int(input("Enter e: "))
if gcd(e, phi) == 1:
    d = pow(e, -1, phi)
    print("n =", n)
    print("phi =", phi)
    print("Public Key =", (e, n))
    print("Private Key =", (d, n))
    message = int(input("Enter message: "))
    cipher = pow(message, e, n)
    print("Encrypted:", cipher)
    plain = pow(cipher, d, n)
    print("Decrypted:", plain)
else:
    print("Invalid e")




