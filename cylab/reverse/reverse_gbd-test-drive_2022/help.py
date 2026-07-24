def decrypt_rotate(encrypted):
    result = ""
    for c in encrypted:
        if 32 < ord(c) < 127:
            # Reverse the rotation
            dec = ord(c) - 0x2f
            if dec <= 32:
                dec += 0x5e
            result += chr(dec)
        else:
            result += c
    return result

# Your encrypted flag from the binary
encrypted = "A:4@r%uL5b3F88bC05C`Gb0fffe5fdgN"  # The data at rbp-0x30

print(decrypt_rotate(encrypted))