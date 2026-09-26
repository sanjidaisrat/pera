# Modular Arithmetic using Primitive Root
p = int(input("Enter modulus: "))
g = int(input("Enter primitive root: "))
print("Primitive Root:", g)
print("Modulus:", p)
print("\nPowers and Modular Results:")

for i in range(1, p):
    result = (g ** i) % p
    print(g, "^", i, "mod", p, "=", result)

