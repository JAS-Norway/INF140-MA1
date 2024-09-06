
def encrypt(plaintext, keystream):
    ciphertext = ""
    plaintextLength = len(plaintext)
    for x in range(plaintextLength):
        newLetterInt = (ord(plaintext[x])-97) + (ord(keystream[x])-97)
        newLetterInt = newLetterInt % 26
        ciphertext += chr(newLetterInt+97)
    return ciphertext

def decrypt(ciphertext, keystream):
    plaintext = ""
    ciphertextLength = len(ciphertext)
    for x in range(ciphertextLength):
        newLetterInt = (ord(ciphertext[x])-97) - (ord(keystream[x])-97)
        if newLetterInt < 0:
            newLetterInt += 26
        newLetterInt = newLetterInt % 26
        plaintext += chr(newLetterInt+97)
    return plaintext


inputText = input("What do you want to encrypt/decrypt? ").lower().replace(" ", "")
key = input("What is the key? ").lower().replace(" ", "")
encryptOrDecrypt = input("Write 'e' to encrypt or 'd' to decrypt: ")

inputTextLength = len(inputText)
keyLength = len(key)

while True:
    if(keyLength >= inputTextLength):
        break
    else:
        key += key
        keyLength = len(key)

if(encryptOrDecrypt == "e"):
    print(encrypt(inputText, key))
elif(encryptOrDecrypt == "d"):
    print(decrypt(inputText, key))
else:
    print("Wrong input.")
    exit()
