 
1. Caesar Cipher
File: lab1.py   |   Classical shift-based monoalphabetic substitution cipher
Theory
The Caesar Cipher is one of the oldest known encryption techniques, named after Julius Caesar, who reportedly used it to protect military messages. It works by shifting every letter of the plaintext a fixed number of positions down (or up) the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on, wrapping around from 'Z' back to 'A'. Mathematically, encryption can be expressed as C = (P + k) mod 26, where P is the plaintext letter's numeric position, k is the shift value (the key), and C is the resulting ciphertext letter. Decryption simply reverses the process: P = (C - k) mod 26. Because the key is a single number between 0 and 25, the Caesar Cipher has an extremely small key space of only 26 possibilities. This makes it trivial to break using a brute-force attack, where every possible shift is tried until a meaningful message appears. It is not used for real security today but remains an important teaching tool for understanding the basic idea of substitution ciphers, modular arithmetic in cryptography, and why key space size matters for security.
Source Code
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
 
 
 

2. Caesar Cipher Cryptanalysis (Brute-Force Attack)
File: labno05.py   |   Breaking the Caesar cipher by exhaustive key search
Theory
This program demonstrates a classic cryptanalysis technique against the Caesar Cipher: the brute-force attack, also called exhaustive key search. Since the Caesar Cipher's key space is only 26 possible shift values, an attacker who has intercepted a ciphertext does not need to know the key in advance — they can simply try every possible shift (0 through 25) and decrypt the message with each one. Among the 26 resulting outputs, only one will typically produce readable, meaningful text (assuming the plaintext was in a natural language like English), and that output reveals both the original message and the key that was used. This attack works specifically because the Caesar Cipher's key space is tiny; algorithms with much larger key spaces (such as AES with a 128-bit key) are computationally infeasible to break this way, since the number of possibilities to check would be astronomically large. This exercise is a foundational example of why cryptographic strength is closely tied to key space size, and it illustrates the general concept of a 'known-ciphertext' attack in cryptanalysis.
Source Code
def decrypt(text, shift): 
    result = "" 
    for ch in text: 
        if ch.isalpha(): 
            result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a')) 
        else: 
            result += ch 
    return result 
cipher = input("Enter encrypted message: ") 
for shift in range(26): 
    print("Shift", shift, ":", decrypt(cipher, shift))

3. Vernam Cipher (Additive Cipher)
File: lab2.py   |   Addition-based polyalphabetic cipher, related to the one-time pad
Theory
The Vernam Cipher, also known as the Additive Cipher, encrypts a message by adding the numeric value of each plaintext letter (A=0, B=1, ..., Z=25) to the numeric value of the corresponding letter in a key, then taking the result modulo 26. Formally, C_i = (P_i + K_i) mod 26 for each position i. Decryption reverses this: P_i = (C_i - K_i) mod 26. Unlike the Caesar Cipher, where a single shift value is reused for every letter, here each letter of the plaintext is combined with a different letter from the key, making the cipher polyalphabetic rather than monoalphabetic. When the key is exactly as long as the message, is completely random, and is used only once — never reused for another message — this scheme becomes the famous one-time pad, which has been mathematically proven to be perfectly secure (unbreakable), because the ciphertext gives no statistical information about the plaintext without knowledge of the key. In practice, however, generating and safely distributing truly random keys as long as the message is difficult, so most real systems approximate this idea with shorter, repeating keys (as in the Vigenère cipher), which reintroduces vulnerability to frequency-based attacks.
Source Code
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

4. Monoalphabetic Substitution Cipher
File: labno03.py   |   Fixed random letter-to-letter mapping
Theory
A monoalphabetic substitution cipher replaces each letter of the plaintext with a corresponding letter from a fixed substitution alphabet, defined by a mapping table (the key). Unlike the Caesar Cipher, where the mapping is generated by a simple numeric shift, here the mapping can be any arbitrary rearrangement of the 26 letters. This dramatically increases the key space to 26 factorial (approximately 4×10²⁶ possible keys), making brute-force attacks computationally infeasible. However, the cipher preserves the statistical frequency pattern of the underlying language — for example, in English, the letter 'E' appears far more often than 'Z' — so even though the mapping is disguised, the frequency of each ciphertext symbol still mirrors the frequency of whichever plaintext letter it represents. This allows cryptanalysts to use frequency analysis, comparing the frequency of symbols in the ciphertext against known letter frequencies of the language, to gradually deduce the substitution mapping and recover the plaintext without ever knowing the key directly. This is why monoalphabetic substitution, despite its large key space, is still considered cryptographically weak by modern standards.
Source Code
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
 
 

5. Playfair Cipher
File: labno06.py   |   Digraph (letter-pair) substitution cipher
Theory
The Playfair Cipher is a manual symmetric encryption technique that was one of the first practical digraphic substitution ciphers, meaning it encrypts pairs of letters (digraphs) together rather than single letters. This makes simple frequency analysis of individual letters far less effective, since the same plaintext letter can map to different ciphertext letters depending on its partner. The cipher builds a 5x5 key square by filling in the letters of a keyword (removing duplicates) followed by the remaining letters of the alphabet, treating 'I' and 'J' as the same letter to fit 26 letters into 25 cells. To encrypt a pair of letters, three rules apply: if both letters lie in the same row, each is replaced by the letter immediately to its right (wrapping around); if both lie in the same column, each is replaced by the letter immediately below (wrapping around); and if they form a rectangle, each letter is replaced by the letter in its own row but in the other letter's column. Decryption applies the same rules in reverse (left instead of right, up instead of down). The Playfair Cipher was actually used for real military communication (notably by the British in World War I) because it was significantly more resistant to manual cryptanalysis than simple substitution ciphers, though it can still be broken with sufficient ciphertext using digraph frequency analysis.
Source Code
def playfair(text, key, decrypt=False): 
    key = key.upper() 
    text = text.upper().replace(" ", "") 
 
    table = "" 
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ": 
        if c not in table: 
            table += c 
 
    result = "" 
    step = -1 if decrypt else 1 
 
    for i in range(0, len(text), 2): 
        a, b = text[i], text[i+1] 
        x, y = table.index(a), table.index(b) 
 
        r1, c1 = x // 5, x % 5 
        r2, c2 = y // 5, y % 5 
 
        if r1 == r2: 
            result += table[r1*5 + (c1+step)%5] 
            result += table[r2*5 + (c2+step)%5] 
 
        elif c1 == c2: 
            result += table[((r1+step)%5)*5+c1] 
            result += table[((r2+step)%5)*5+c2] 
 
        else: 
            result += table[r1*5+c2] 
            result += table[r2*5+c1] 
 
    return result 
 
 
key = input("Enter key: ") 
msg = input("Enter message: ") 
 
encrypted = playfair(msg, key) 
decrypted = playfair(encrypted, key, True) 
 
print("Encrypted:", encrypted) 
print("Decrypted:", decrypted)

6. Hill Cipher
File: labno07.py   |   Matrix-multiplication-based polygraphic cipher
Theory
The Hill Cipher is a polygraphic substitution cipher based on linear algebra, invented by Lester Hill in 1929. It represents the encryption key as an n×n matrix of integers (mod 26), and encrypts the plaintext in blocks of n letters at a time. Each block of n letters is treated as a numeric column vector, which is multiplied by the key matrix (with all arithmetic performed modulo 26) to produce the corresponding ciphertext block. For decryption, the recipient needs the modular multiplicative inverse of the key matrix; multiplying the ciphertext vector by this inverse matrix recovers the original plaintext vector. Because the key matrix must be invertible modulo 26 (its determinant must be coprime with 26), not every matrix can serve as a valid Hill Cipher key. The major strength of the Hill Cipher compared to earlier ciphers is that it encrypts multiple letters simultaneously and diffuses the influence of each plaintext letter across several ciphertext letters, making simple frequency analysis of single letters ineffective. However, it remains vulnerable to known-plaintext attacks, since if enough plaintext-ciphertext pairs are known, the key matrix itself can be recovered algebraically.
Source Code
import numpy as np 
 
K = np.array([[3,3],[2,5]]) 
I = np.array([[15,17],[20,9]]) 
 
def hill(text, key): 
    text = text.upper().replace(" ","") 
    if len(text)%2: text += "X" 
    result = "" 
 
    for i in range(0,len(text),2): 
        a = ord(text[i])-65 
        b = ord(text[i+1])-65 
        x = key @ [a,b] 
        result += chr(x[0]%26+65) + chr(x[1]%26+65) 
 
    return result 
 
msg = input("Enter message: ") 
cipher = hill(msg,K) 
 
print("Encrypted:", cipher) 
print("Decrypted:", hill(cipher,I))

7. Columnar Transposition Cipher (Double Transposition)
File: labno08.py   |   Position-rearrangement cipher applied twice for extra security
Theory
Unlike substitution ciphers, which replace letters with other letters, a transposition cipher keeps the original letters unchanged but rearranges their positions according to a systematic rule. In the columnar transposition cipher, the plaintext is conceptually written into a grid with a number of columns equal to the key, and the ciphertext is produced by reading the letters column by column instead of row by row. A single round of columnar transposition can be broken relatively easily by an analyst who tries different numbers of columns and looks for readable patterns, or through anagramming techniques. To increase resistance to cryptanalysis, this program applies double transposition: the plaintext is first transposed using one key, and the resulting intermediate ciphertext is transposed a second time using a different key. This double application significantly increases the complexity of the resulting permutation, since the effective permutation is now a composition of two separate rearrangements, making it much harder for an attacker to reconstruct the original column order and recover the plaintext. Historically, double transposition ciphers were used in real-world military and diplomatic communications, including by the German army in both World Wars, precisely because of this added strength over a single transposition.
Source Code
#columnar er code 
def encrypt(text, key): 
    result = "" 
 
    for col in range(key): 
        for i in range(col, len(text), key): 
            result += text[i] 
 
    return result 
message = input("Enter message: ") 
key1 = int(input("Enter first key: ")) 
key2 = int(input("Enter second key: ")) 
step1 = encrypt(message, key1) 
step2 = encrypt(step1, key2) 
print("First encryption :", step1) 
print("Final encryption :", step2) 
 
 

8. GCD — Euclidean Algorithm
File: labno04.py   |   Classical method for computing the greatest common divisor
Theory
The Euclidean Algorithm is an efficient method, dating back over 2000 years to Euclid's 'Elements', for computing the greatest common divisor (GCD) of two integers. It relies on the key mathematical fact that gcd(a, b) = gcd(b, a mod b), and that gcd(a, 0) = a. By repeatedly replacing the pair (a, b) with (b, a mod b) until the second value becomes zero, the algorithm converges on the GCD in a number of steps that is logarithmic relative to the size of the inputs, making it far more efficient than naive approaches like checking all possible divisors. In cryptography, the Euclidean Algorithm plays a foundational role: it is used to verify that two numbers are coprime (i.e., that their GCD equals 1), which is a required condition in algorithms such as RSA, where the public exponent e must be coprime with Euler's totient φ(n) for the key generation process to produce a valid, invertible private exponent.
Source Code
# GCD using Euclidean Algorithm 
 
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
while b != 0: 
    a, b = b, a % b 
print("GCD =", a)

9. Extended Euclidean Algorithm
File: E-2-5.py   |   Computing GCD along with Bézout coefficients (x, y)
Theory
The Extended Euclidean Algorithm is an extension of the classical Euclidean Algorithm that not only computes the greatest common divisor of two integers a and b, but also finds a pair of integers x and y such that ax + by = gcd(a, b). This equation is known as Bézout's Identity, and the algorithm computes it recursively by working backward through the sequence of divisions performed during the standard Euclidean Algorithm (a technique often called back-substitution). This algorithm is of central importance in cryptography because it provides a constructive way to compute modular multiplicative inverses: if gcd(e, n) = 1, then the Extended Euclidean Algorithm can find an integer d such that e*d ≡ 1 (mod n), meaning d is the modular inverse of e modulo n. This is precisely the computation needed to derive the private exponent d in RSA from the public exponent e and Euler's totient φ(n), making the Extended Euclidean Algorithm an essential building block underlying modern public-key cryptography.
Source Code
 
def extended_gcd(a, b): 
    if b == 0: 
        return a, 1, 0 
    r = a % b 
    q = a // b 
    gcd, x1, y1 = extended_gcd(b, r) 
    x = y1 
    y = x1 - q * y1 
    return gcd, x, y 
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
gcd, x, y = extended_gcd(a, b) 
print("GCD:", gcd) 
print("x:", x) 
print("y:", y) 
print("Verification:", a*x + b*y)

10. Primitive Root and Modular Exponentiation
File: E-2-4.py   |   Generating the full residue set of a prime modulus
Theory
This program explores the concept of a primitive root (also called a generator) modulo a prime number p. An integer g is said to be a primitive root modulo p if the sequence of its successive powers — g¹, g², g³, ..., g^(p-1), all taken modulo p — produces every nonzero residue from 1 to p-1 exactly once before repeating. In other words, g 'generates' the entire multiplicative group of integers modulo p. This property is fundamental to several widely used public-key cryptosystems, including the Diffie-Hellman key exchange and ElGamal encryption, both of which rely on a publicly known prime p and a primitive root g as the basis for generating public and private keys. The security of these systems ultimately depends on the difficulty of the discrete logarithm problem: given g, p, and g^x mod p, it is computationally very difficult to determine x, even though computing g^x mod p itself is easy. Verifying that a chosen g is indeed a primitive root (by checking that its powers cover the full residue range without repetition) is therefore an important step before using it as a cryptographic parameter.
Source Code
# Modular Arithmetic using Primitive Root 
p = int(input("Enter modulus: ")) 
g = int(input("Enter primitive root: ")) 
print("Primitive Root:", g) 
print("Modulus:", p) 
print("\nPowers and Modular Results:") 
 
for i in range(1, p): 
    result = (g ** i) % p 
    print(g, "^", i, "mod", p, "=", result) 
 
 

11. DES (Data Encryption Standard)
File: E-2-1.py   |   Symmetric-key block cipher operating in ECB mode
Theory
DES (Data Encryption Standard) is a symmetric-key block cipher developed in the 1970s and adopted as a U.S. federal standard, which became one of the most widely used encryption algorithms of the 20th century. It processes data in fixed-size blocks of 64 bits and uses a 64-bit key, of which only 56 bits are effectively used for encryption (the remaining 8 bits serve as parity-check bits rather than contributing to security). Internally, DES applies a Feistel network structure across 16 rounds, where in each round the data block is split in half, one half is transformed using a round-specific subkey and combined with the other half, and the halves are swapped — this repeated mixing and substitution provides both confusion and diffusion, two properties considered essential for cipher security. This particular implementation uses ECB (Electronic Codebook) mode, the simplest block cipher mode of operation, in which each block of plaintext is encrypted independently using the same key. While simple to implement, ECB mode has a well-known weakness: identical plaintext blocks always produce identical ciphertext blocks, which can leak structural patterns in the underlying data (this is famously illustrated by encrypting an image in ECB mode and still being able to make out its shapes in the ciphertext). Additionally, DES's 56-bit effective key length is now considered far too short for modern security requirements, since it can be brute-forced by modern computing hardware in a matter of hours; as a result, DES has been officially deprecated and replaced by the Advanced Encryption Standard (AES) for virtually all real-world applications.
Source Code
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
 

12. RSA Algorithm
File: E-2-2.py   |   Public-key cryptosystem based on integer factorization
Theory
RSA, named after its inventors Rivest, Shamir, and Adleman, is one of the first and most widely deployed public-key (asymmetric) cryptosystems. Its security rests on the computational difficulty of factoring the product of two large prime numbers. Key generation begins by selecting two distinct large primes p and q, computing their product n = p*q (which serves as the modulus), and computing Euler's totient φ(n) = (p-1)(q-1). A public exponent e is then chosen such that 1 < e < φ(n) and gcd(e, φ(n)) = 1, ensuring e has a valid modular inverse. The private exponent d is computed as the modular multiplicative inverse of e modulo φ(n), typically using the Extended Euclidean Algorithm. The pair (n, e) forms the public key, which can be freely shared, while (n, d) forms the private key, which must be kept secret. Encryption of a numeric message m is performed as c = m^e mod n, and decryption recovers the original message as m = c^d mod n. This works due to a property derived from Euler's theorem in number theory, guaranteeing that (m^e)^d ≡ m (mod n) whenever the keys are generated correctly. RSA's security fundamentally depends on the fact that, while multiplying two large primes together is computationally easy, factoring their product back into the original primes is computationally very hard for sufficiently large numbers (typically 2048 bits or more in real-world use), which is why key sizes must be kept large as computing power increases.
Source Code
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
 
 
 
 
 

13. Diffie–Hellman Key Exchange
File: E-2-3.py   |   Protocol for establishing a shared secret over a public channel
Theory
The Diffie-Hellman key exchange, published in 1976, was the first practical method allowing two parties to establish a shared secret key over a completely public and insecure communication channel, without ever transmitting the secret key itself. The protocol begins with two publicly agreed-upon values: a large prime p and a generator (primitive root) g. Each party independently chooses a secret private key (commonly labeled a for Alice and b for Bob) and computes a corresponding public key by raising g to the power of their private key modulo p (A = g^a mod p, B = g^b mod p). The two parties then exchange these public keys openly. To derive the shared secret, each party raises the other party's public key to the power of their own private key: Alice computes B^a mod p, and Bob computes A^b mod p. Due to the properties of modular exponentiation, both computations yield the same result, g^(ab) mod p, which becomes the shared secret key used for subsequent symmetric encryption. The security of this scheme relies entirely on the discrete logarithm problem: even though an eavesdropper can observe p, g, A, and B, recovering the private exponents a or b from these public values is computationally infeasible for sufficiently large parameters, since there is no known efficient algorithm to reverse modular exponentiation in this way.
Source Code
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

14. ElGamal Encryption
File: labno09.py   |   Discrete-logarithm-based public-key encryption
Theory
ElGamal encryption, proposed by Taher ElGamal in 1985, is a public-key cryptosystem whose security, like Diffie-Hellman, is based on the difficulty of the discrete logarithm problem in a finite cyclic group. Key generation uses a publicly known prime p and generator g; the recipient chooses a private key x and publishes the corresponding public key y = g^x mod p. To encrypt a message m, the sender selects a fresh random value k for every encryption (this randomness is essential to security) and computes two ciphertext components: c1 = g^k mod p and c2 = (m * y^k) mod p. The pair (c1, c2) is sent as the ciphertext. To decrypt, the recipient uses their private key x to compute the shared value s = c1^x mod p, which is mathematically equal to y^k mod p that the sender used during encryption, and then computes the modular multiplicative inverse of s to recover the plaintext: m = (c2 * s⁻¹) mod p. A distinguishing feature of ElGamal is that it is a probabilistic encryption scheme: because a new random k is used every time, encrypting the same plaintext message twice produces two completely different ciphertexts, which prevents certain types of pattern-based attacks that deterministic schemes (like plain RSA) can be vulnerable to. The main trade-off is that ElGamal ciphertexts are roughly twice the size of the plaintext, since two values (c1 and c2) must be transmitted for every encrypted message.
Source Code
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

