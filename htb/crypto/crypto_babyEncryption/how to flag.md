Category: Cryptography

Topic: Affine cipher over modulus 256 with linear transformation

Vulnerability:
Weak Affine Cipher – The encryption uses a simple linear function:

```
c = (a * m + b) mod 256
where a = 123 and b = 18. 
```

Since the modulus is small (256) and the transformation is linear, it's trivially invertible when gcd(a, 256) = 1.

Exploit
Use the solve.py brute forcing script to get the flag

Flag got: HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}


Prevention / Mitigation
- Use strong encryption algorithms (AES, ChaCha20)
- Never roll your own crypto
- Use proper key sizes and secure random number generators
- If using affine cipher, use it only as a component of a larger system