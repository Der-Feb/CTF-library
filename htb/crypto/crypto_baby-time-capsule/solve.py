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
    time.sleep(0.2)
    
    # Receive response (JSON + newline)
    response = recv_until(s, b'\n').decode().strip()
    
    # Clean up if prompt got mixed in
    if '(Y/n)' in response:
        response = response.split('(Y/n)')[0].strip()
    if 'Welcome' in response:
        response = response.split('Welcome')[0].strip()
    
    try:
        capsule = json.loads(response)
        c = int(capsule['time_capsule'], 16)
        n = int(capsule['pubkey'][0], 16)
        ciphertexts.append(c)
        moduli.append(n)
        print(f"[+] Got capsule {i+1}/5")
    except json.JSONDecodeError:
        print(f"[!] Failed to parse: {response[:100]}")
        print("[!] Trying again...")
        # Try one more time
        time.sleep(0.5)
        response = recv_until(s, b'\n').decode().strip()
        capsule = json.loads(response)
        c = int(capsule['time_capsule'], 16)
        n = int(capsule['pubkey'][0], 16)
        ciphertexts.append(c)
        moduli.append(n)
        print(f"[+] Got capsule {i+1}/5 (retry)")

s.close()

print(f"\n[+] Collected {len(ciphertexts)} capsules")

if len(ciphertexts) >= 5:
    print("[+] Running CRT attack...")
    m5 = chinese_remainder(moduli[:5], ciphertexts[:5])
    
    print("[+] Computing 5th root...")
    flag_int, exact = gmpy2.iroot(m5, 5)
    
    if not exact:
        print("[!] Root not exact, searching nearby...")
        for offset in range(-1000, 1000):
            test = flag_int + offset
            if pow(test, 5) == m5:
                flag_int = test
                exact = True
                break
    
    flag_bytes = long_to_bytes(flag_int)
    
    # Try to decode as flag
    try:
        flag = flag_bytes.decode('utf-8')
        print(f"\n🏁 FLAG: {flag}")
    except:
        # If it's not valid UTF-8, try to find HTB in the bytes
        flag_str = flag_bytes.decode('latin-1')
        if 'HTB' in flag_str:
            start = flag_str.find('HTB')
            end = flag_str.find('}', start) + 1
            print(f"\n🏁 FLAG: {flag_str[start:end]}")
        else:
            print(f"\n[!] Raw bytes: {flag_bytes}")
else:
    print("[!] Not enough capsules collected")