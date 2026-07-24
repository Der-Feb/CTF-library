def decrypt(encrypted_hex, key="S3Cr3t"):
    encrypted_bytes = bytes.fromhex(encrypted_hex)  # <-- Add this line
    plaintext = []
    for i, byte in enumerate(encrypted_bytes):
        plaintext.append(byte ^ ord(key[i % len(key)]))
    return ''.join(chr(c) for c in plaintext)

user_flag = input("Enter the encrypted hex: ")
flag = decrypt(user_flag)
print("flag:", flag)