# Aim :  Implement Caesar cipher encryption-decryption

def caesar_cipher_encrypt(text, shift): 
    result = "" 
    for char in text: 
        if char.isalpha():  
            start = ord('A') if char.isupper() else ord('a') 
            result += chr((ord(char) - start + shift) % 26 + start) 
        else: 
            # Non-alphabetic characters remain the same 
            result += char 
    return result 
 
def caesar_cipher_decrypt(cipher_text, shift): 
    return caesar_cipher_encrypt(cipher_text, -shift) 
 
plain_text = input("ENTER THE PLAIN TEXT : ") 
shift_value = int(input("ENTER THE KEY VALUE : ")) 
encrypted_text = caesar_cipher_encrypt(plain_text, shift_value) 
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value) 
print("Original Text:", plain_text) 
print("Encrypted Text:", encrypted_text) 
print("Decrypted Text:", decrypted_text)