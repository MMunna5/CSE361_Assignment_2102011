def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        index = ord(char) - 65  # 0-25
        shifted = (index + key) % 26
        binary = format(shifted, '05b')
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
        new_index = int(inverted, 2) % 26
        ciphertext += chr(65 + new_index)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext.upper():
        index = ord(char) - 65
        binary = format(index, '05b')
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
        original_index = int(inverted, 2) % 26
        decrypted = (original_index - key + 26) % 26
        plaintext += chr(65 + decrypted)
    return plaintext

# Test
plaintext = "HELLO"
key = 3
ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
