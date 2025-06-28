# Aim :  Implement Playfair cipher encryption-decryption

def generate_key_matrix(key): 
    key = key.upper().replace("J", "I") 
    key_matrix = [] 
    used = set() 
 
    for char in key: 
        if char not in used and char.isalpha(): 
            used.add(char) 
            key_matrix.append(char) 
 
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ": 
        if char not in used: 
            used.add(char) 
            key_matrix.append(char) 
 
    return [key_matrix[i*5:(i+1)*5] for i in range(5)] 
 
def prepare_text(text, for_encryption=True): 
    text = text.upper().replace("J", "I") 
    result = "" 
    i = 0 
    while i < len(text): 
        a = text[i] 
        b = ' ' 
        if i + 1 < len(text): 
            b = text[i + 1] 
        if a == b: 
            result += a + 'X' 
            i += 1 
        else: 
            result += a 
            if i + 1 < len(text): 
                result += b 
            i += 2 
    if len(result) % 2 != 0: 
        result += 'X' 
    return result 
 
def find_position(matrix, char): 
    for row in range(5): 
        for col in range(5): 
            if matrix[row][col] == char: 
                return row, col 
    return None 
 
def encrypt_pair(a, b, matrix): 
    r1, c1 = find_position(matrix, a) 
    r2, c2 = find_position(matrix, b) 
 
    if r1 == r2: 
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5] 
    elif c1 == c2: 
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2] 
    else: 
        return matrix[r1][c2] + matrix[r2][c1] 
 
def decrypt_pair(a, b, matrix): 
    r1, c1 = find_position(matrix, a) 
    r2, c2 = find_position(matrix, b) 
 
    if r1 == r2: 
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5] 
    elif c1 == c2: 
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2] 
    else: 
        return matrix[r1][c2] + matrix[r2][c1]
def encrypt(text, key): 
    matrix = generate_key_matrix(key) 
    prepared = prepare_text(text) 
    result = '' 
    for i in range(0, len(prepared), 2): 
        result += encrypt_pair(prepared[i], prepared[i+1], matrix) 
    return result 
 
def decrypt(cipher, key): 
    matrix = generate_key_matrix(key) 
    result = '' 
    for i in range(0, len(cipher), 2): 
        result += decrypt_pair(cipher[i], cipher[i+1], matrix) 
    return result 
 
key = input("Enter the key: ") 
choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper() 
 
if choice == 'E': 
    plaintext = input("Enter the plaintext: ") 
    cipher = encrypt(plaintext, key) 
    print("Encrypted Text:", cipher) 
 
elif choice == 'D':
    ciphertext = input("Enter the ciphertext: ") 
    plain = decrypt(ciphertext, key) 
    print("Decrypted Text:", plain) 
else: 
    print("Invalid choice. Please enter E or D.") 