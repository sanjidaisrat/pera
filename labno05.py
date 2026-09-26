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