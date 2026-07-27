import hashlib
import sys

with open("cheeses.txt") as f:
    CHEESES = [line.strip() for line in f if line.strip()]


def crack(target_hash):
    target_hash = target_hash.strip().lower()
    for salt_int in range(256):
        salt_byte = bytes([salt_int])
        salt_hex = format(salt_int, '02x')
        for name in CHEESES:
            if hashlib.sha256(name.lower().encode() + salt_byte).hexdigest() == target_hash:
                return name, salt_hex
    return None, None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        h = sys.argv[1]
    else:
        h = input("Paste the hash: ").strip()

    name, salt = crack(h)
    if name is None:
        print("No match found.")
    else:
        print(f"cheese = {name}")
        print(f"salt   = {salt}")
