#!/usr/bin/env python3

with open('flag.txt.enc', 'rb') as f:
    data = f.read()

def xor_decrypt(data, key):
    extended_key = key
    i = 0
    while len(extended_key) < len(data):
        extended_key = extended_key + key[i]
        i = (i + 1) % len(key)
    
    result = []
    for byte, key_char in zip(data, extended_key):
        result.append(chr(byte ^ ord(key_char)))
    return ''.join(result)

# Try the full word
key = "rapscallion"
decrypted = xor_decrypt(data, key)
print(f"Key: {key}")
print(f"Flag: {decrypted}")

# Also print to see if any characters need fixing
print(f"\nRaw repr: {repr(decrypted)}")