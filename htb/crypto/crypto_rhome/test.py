from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import math
from hashlib import sha256

# Given Parameters

g = int(input("Enter the \"g\" parameters: "))
p = int(input("Enter the \"p\" parameters: "))
A = int(input("Enter the \"A\" parameters: "))
B = int(input("Enter the \"B\" parameters: "))
ct_hex = input("Enter encrypted flag:  ")

def baby_step_giant_step(g, target, p, order_bound):
    """Solves g^x = target mod p using Baby-step Giant-step."""
    m = int(math.ceil(math.sqrt(order_bound)))
    
    print("[+] Computing baby steps...")
    lookup = {}
    current = 1
    for j in range(m):
        lookup[current] = j
        current = (current * g) % p
        
    print("[+] Computing giant steps...")
    # g^(-m) mod p
    g_inv_m = pow(g, p - 1 - m, p)
    
    current = target
    for i in range(m):
        if current in lookup:
            return i * m + lookup[current]
        current = (current * g_inv_m) % p
    return None

# The source code specified a 42-bit prime for q (the order of g)
order_bound = 2**42

print("[+] Launching Baby-step Giant-step...")
a = baby_step_giant_step(g, A, p, order_bound)

if a is not None:
    print(f"[+] Found private key a: {a}")
    
    # ss = B^a mod p
    shared_secret = pow(B, a, p)
    print(f"[+] Computed Shared Secret: {shared_secret}")
    
    # Decrypting flag
    key = sha256(long_to_bytes(shared_secret)).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(bytes.fromhex(ct_hex))
    
    # Strip PKCS7 padding
    padding_len = pt[-1]
    clean_flag = pt[:-padding_len].decode('utf-8', errors='ignore')
    print(f"\n[+] Flag: {clean_flag}")
else:
    print("[-] Failed to find private key within the 42-bit bound.")