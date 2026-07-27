
## Category
Cryptography

## Topic 
SHA256 hash of the timestamp

## Vulnerability
The encryption key is derived from the current Unix timestamp using SHA256, but the timestamp parameter is ignored and overwritten with time.time(), making the key predictable within a small time window.

## Exploit
Since we know the approximate timestamp (1770242610), we brute-force a small range of timestamps around it (e.g., ±60 seconds), regenerate the AES-ECB key for each, and decrypt the ciphertext until we get valid plaintext containing the flag.

You can just run the decrypt.py to get the flag

Found at timestamp: 1770242610
Plaintext: picoCTF{sa3S_sEc9t_91609b3c}

=> picoCTF{sa3S_sEc9t_91609b3c}