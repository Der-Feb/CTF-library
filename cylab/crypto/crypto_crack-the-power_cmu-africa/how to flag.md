## Category
Cryptography

## Topic
Low Public Exponent RSA Attack (Coppersmith's attack)

## Vulnerability: 
The public exponent e = 20 is unusually small and shares factors with the totient, making the encryption a low-exponent RSA where we can recover the plaintext by taking the 20th root of the ciphertext without factoring n.

## Exploit: 
Since e = 20 and the message is likely much smaller than n, we can compute the integer 20th root of the ciphertext to recover the plaintext directly (if m^20 < n, which is true for small messages).

You can use the decrypt.py python script to get the flag
=> picoCTF{t1ny_e_f053d79c}