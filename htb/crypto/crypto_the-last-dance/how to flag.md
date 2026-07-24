
Category: Cryptography

Topic: ChaCha20 stream cipher encryption with reused nonce (IV)

Vulnerability: Nonce Reuse (IV Reuse) – The same key and nonce are used to encrypt two different plaintexts (a known message and the flag). In stream ciphers like ChaCha20, reusing the same key and nonce generates identical keystreams, allowing an attacker to recover plaintext via XOR operations.

Exploit:
Given data:
Nonce (IV): c4a66edfe80227b4fa24d431
Encrypted known message (hex)
Encrypted flag (hex)
Recover Keystream:
Known plaintext is provided in the source code
Compute: keystream = known_plaintext XOR encrypted_known_message
Decrypt Flag:
Compute: flag = encrypted_flag XOR keystream

=> HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}

Prevention / Mitigation
- Always use a unique nonce for each encryption with the same key
- Use a counter-based nonce or random nonce with sufficient entropy
- Never reuse key-nonce pairs in stream ciphers
