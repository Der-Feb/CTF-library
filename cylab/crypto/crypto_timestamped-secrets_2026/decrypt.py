from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

ciphertext_hex = "71cd3848348a45b82789f710c3321aceab2171e004200b57fe9cc64d4ea33cec"
ciphertext = bytes.fromhex(ciphertext_hex)

# Try the exact timestamp and a few around it
for timestamp in range(1770242600, 1770242621):
    key = sha256(str(timestamp).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    
    try:
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        plaintext = decrypted.decode('utf-8')
        if 'picoCTF' in plaintext:
            print(f"Found at timestamp: {timestamp}")
            print(f"Plaintext: {plaintext}")
            break
    except:
        pass