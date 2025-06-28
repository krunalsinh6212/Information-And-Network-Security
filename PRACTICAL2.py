# Aim :  Implement Monoalphabetic cipher encryption - decryption 

import string 
 
alphabet = string.ascii_lowercase 
key = "phqgiumeaylnofdxjkrcvstzwb" 
 
def encrypt(plaintext, key): 
    ciphertext = "" 
    for char in plaintext.lower(): 
        if char in alphabet: 
            index = alphabet.index(char) 
            ciphertext += key[index] 
        else: 
            ciphertext += char   
    return ciphertext 
 
def decrypt(ciphertext, key): 
    plaintext = "" 
    for char in ciphertext.lower(): 
        if char in key: 
            index = key.index(char)
            plaintext += alphabet[index] 
        else: 
            plaintext += char 
    return plaintext 

text = input() 
cipher = encrypt(text, key) 
print("Encrypted:", cipher) 
original = decrypt(cipher, key) 
print("Decrypted:", original)