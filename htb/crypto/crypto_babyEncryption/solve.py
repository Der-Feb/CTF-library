with open('msg.enc', 'r') as f:
    hex_data = f.read().strip()
    ct = bytes.fromhex(hex_data)

# Try to find flag by looking for 'HTB' pattern
for a in range(1, 256, 2):  # must be odd for invertibility
    for b in range(256):
        try:
            dec = ''.join(chr(((c - b) * pow(a, -1, 256)) % 256) for c in ct)
            if 'HTB' in dec:
                print(f"Found! a={a}, b={b}")
                print(dec)
                break
        except:
            continue
        
