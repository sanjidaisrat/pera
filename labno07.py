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