# RSA Small Exponent Broadcast Attack

**Category:** Cryptography
**Topic:** RSA encryption with small public exponent (Håstad's Broadcast Attack)

## Vulnerability

**Small Exponent Attack (Håstad's Broadcast Attack)** — The server uses a very small public exponent `e = 5` and allows unlimited requests for time capsules. Each request generates a new modulus `n`, but encrypts the same flag with the same small exponent every time. When the same message is encrypted with the same small exponent under multiple different moduli, an attacker can recover the plaintext using the Chinese Remainder Theorem (CRT) without needing to factor any modulus.

## Exploit

### Step 1: Connect to the server and collect 5 capsules

```bash
nc 154.57.164.61 31587
```

Type `Y` five times to get 5 different encrypted capsules.

### Step 2: Extract ciphertexts and moduli

Each response contains:

- `time_capsule`: ciphertext `c` in hex
- `pubkey`: `[n, e]` where `n` is the modulus and `e = 5`

### Step 3: Run the attack

```python
import socket
import json
from Crypto.Util.number import long_to_bytes
import gmpy2
from functools import reduce
import time

def chinese_remainder(moduli, remainders):
    prod = reduce(lambda a, b: a * b, moduli)
    total = 0
    for n_i, a_i in zip(moduli, remainders):
        p = prod // n_i
        total += a_i * pow(p, -1, n_i) * p
    return total % prod

def recv_until(sock, delim=b'\n'):
    data = b''
    while delim not in data:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk
    return data

# Target
HOST = '154.57.164.61'
PORT = 31587

print(f"[+] Connecting to {HOST}:{PORT}")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

ciphertexts = []
moduli = []

for i in range(5):
    # Receive prompt
    prompt = recv_until(s, b'(Y/n) ')
    print(f"[*] Requesting capsule {i+1}/5")

    # Send 'Y'
    s.send(b'Y\n')
    time.sleep(0.1)

    # Receive response
    response = recv_until(s, b'\n').decode().strip()

    # Clean up if prompt got mixed in
    if '(Y/n)' in response:
        response = response.split('(Y/n)')[0].strip()

    capsule = json.loads(response)
    c = int(capsule['time_capsule'], 16)
    n = int(capsule['pubkey'][0], 16)
    ciphertexts.append(c)
    moduli.append(n)
    print(f"[+] Got capsule {i+1}/5")

s.close()

print("\n[+] Running CRT attack...")
m5 = chinese_remainder(moduli, ciphertexts)

print("[+] Computing 5th root...")
flag_int, exact = gmpy2.iroot(m5, 5)

if not exact:
    # Try nearby values
    for offset in range(-100, 101):
        test = flag_int + offset
        if pow(test, 5) == m5:
            flag_int = test
            exact = True
            break

flag = long_to_bytes(flag_int)
print(f"\n🏁 FLAG: {flag.decode()}")
```

### Alternative: Manual solution with collected data

```python
from Crypto.Util.number import long_to_bytes
import gmpy2
from functools import reduce

def chinese_remainder(moduli, remainders):
    prod = reduce(lambda a, b: a * b, moduli)
    total = 0
    for n_i, a_i in zip(moduli, remainders):
        p = prod // n_i
        total += a_i * pow(p, -1, n_i) * p
    return total % prod

# Paste your collected capsule data here
data = [
    # 5 capsule JSON objects from netcat
]

ciphertexts = [int(item['time_capsule'], 16) for item in data]
moduli = [int(item['pubkey'][0], 16) for item in data]

m5 = chinese_remainder(moduli, ciphertexts)
flag_int, exact = gmpy2.iroot(m5, 5)
flag = long_to_bytes(flag_int)
print(f"FLAG: {flag.decode()}")
```

## Flag

```
HTB{7de39f595937dfbbea41124450b43370}
```

## Prevention / Mitigation

- Use a large public exponent like `e = 65537` instead of `e = 5`
- Implement proper padding schemes (OAEP) to prevent mathematical attacks
- Randomize the message before encryption (add random padding)
- Never encrypt the exact same plaintext multiple times with the same exponent
- Limit the number of requests a client can make to prevent data collection for broadcast attacks


Use the command: python3 crack.py <your_hashed_key>

=> picoCTF{cHeEsY5a890258}