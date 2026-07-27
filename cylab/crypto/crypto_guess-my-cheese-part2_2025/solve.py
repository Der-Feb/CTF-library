import socket
import hashlib
import re
import sys
import time

HOST = "verbal-sleep.picoctf.net"
PORT = 53283

with open("cheeses.txt") as f:
    CHEESES = [line.strip() for line in f if line.strip()]

HASH_RE = re.compile(r'\b[a-fA-F0-9]{64}\b')


def brute_force(target_hash):
    """sha256(cheese_name.encode() + raw_salt_byte) == target_hash"""
    target_hash = target_hash.lower()
    for salt_int in range(256):
        salt_byte = bytes([salt_int])
        salt_hex = format(salt_int, '02x')
        for name in CHEESES:
            if hashlib.sha256(name.lower().encode() + salt_byte).hexdigest() == target_hash:
                return name, salt_hex
    return None, None


def recv_until(sock, markers, timeout=5):
    """Read until one of the marker substrings shows up (or timeout)."""
    sock.settimeout(timeout)
    data = b""
    end = time.time() + timeout
    while time.time() < end:
        try:
            chunk = sock.recv(4096)
        except socket.timeout:
            break
        if not chunk:
            break
        data += chunk
        text = data.decode(errors="ignore")
        if any(m in text for m in markers):
            break
    return data.decode(errors="ignore")


def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    banner = recv_until(s, ["What would you like to do?"])
    print(banner)

    round_num = 0
    while True:
        round_num += 1
        m = HASH_RE.search(banner)
        if not m:
            print("!! No hash found in output, stopping. Last output above.")
            break
        target_hash = m.group(0)

        # send 'g' to guess
        s.sendall(b"g\n")
        challenge = recv_until(s, ["what's my cheese?"])
        print(challenge)

        m2 = HASH_RE.search(challenge)
        current_hash = m2.group(0) if m2 else target_hash

        name, salt = brute_force(current_hash)
        if name is None:
            print(f"!! Round {round_num}: could not crack hash {current_hash}")
            break
        print(f"[round {round_num}] cheese={name!r} salt={salt}")

        s.sendall((name + "\n").encode())
        after_cheese = recv_until(s, ["what's my salt?"])
        print(after_cheese)

        s.sendall((salt + "\n").encode())
        result = recv_until(s, ["picoCTF{", "GET OUT", "What would you like to do?"], timeout=8)
        print(result)

        if "picoCTF{" in result:
            flag_match = re.search(r'picoCTF\{[^}]*\}', result)
            if flag_match:
                print("\n=== FLAG FOUND ===")
                print(flag_match.group(0))
            break

        if "GET OUT" in result or "yuck" in result.lower():
            print("!! Wrong guess according to server logic - stopping for debugging.")
            break

        # otherwise loop continues, e.g. new hash presented for next round
        banner = result

    s.close()


if __name__ == "__main__":
    run()
