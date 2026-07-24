from Cryptodome.Cipher import AES

with open('0', 'rb') as f:
    data = f.read()

key = data[:32]
iv = data[32:48]
ciphertext = data[48:]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

def read_7bit_int(data, pos):
    result, shift = 0, 0
    while True:
        b = data[pos]; pos += 1
        result |= (b & 0x7f) << shift
        if not (b & 0x80):
            break
        shift += 7
    return result, pos

pos = 0
strings = []
while pos < len(plaintext):
    strlen, pos = read_7bit_int(plaintext, pos)
    s = plaintext[pos:pos+strlen].decode('utf-16-le')
    pos += strlen
    strings.append(s)

for i, s in enumerate(strings):
    print(i, repr(s))