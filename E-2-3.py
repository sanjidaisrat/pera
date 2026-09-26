# Public values
p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))
# Private keys
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))
# Public keys
A = pow(g, a, p)
B = pow(g, b, p)
print("Alice's Public Key:", A)
print("Bob's Public Key:", B)
# Shared secret
secret_alice = pow(B, a, p)
secret_bob = pow(A, b, p)
print("Alice's Shared Secret:", secret_alice)
print("Bob's Shared Secret:", secret_bob)