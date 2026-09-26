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

