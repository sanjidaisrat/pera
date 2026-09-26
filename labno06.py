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