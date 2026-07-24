packed = open('enc', 'r').read()
result = []

for c in packed:
    value = ord(c)

    high = value >> 8
    low = value & 0xFF

    result.append(chr(high))
    result.append(chr(low))

unpacked = ''.join(result)
print(unpacked)