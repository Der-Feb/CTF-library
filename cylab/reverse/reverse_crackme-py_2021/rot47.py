alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
            
def rot47(text):
    result = ""

    for c in text:
        o = ord(c)
        if 33 <= o <= 126:
            result += chr(33 + ((o - 33 + 47) % 94))
        else:
            result += c

    return result

    