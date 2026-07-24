import socket
import re

host = input("Enter the link for example: (mysterious-sea.picoctf.net): ")
port = int(input("Enter the port: "))

def solve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    data = ''
    round_num = 1
    
    while True:
        chunk = s.recv(8192).decode(errors='ignore')
        if not chunk:
            break
        data += chunk
        
        # Look for the pattern: number on its own line, followed by "Here's the next binary"
        # This is the secret
        match = re.search(r'\n(\d+)\nHere\'s the next binary in bytes:', data)
        if match:
            secret = match.group(1)
            # Only send if we haven't sent this one yet
            print(f"Round {round_num}: Secret found: {secret}")
            s.send((secret + '\n').encode())
            round_num += 1
            # Clear the data up to and including the secret line
            data = data.split("Here's the next binary in bytes:", 1)[-1]
            continue
        
        # Check for flag
        if 'picoCTF{' in data:
            flag_match = re.search(r'picoCTF\{[^}]+\}', data)
            if flag_match:
                print(f"\n🎉 FLAG: {flag_match.group(0)}")
                break
        
        # If we see "What's the secret?:" but no pattern matched yet,
        # try to find the secret from the start of data
        if "What's the secret?:" in data:
            # Look for a number at the very beginning of the data
            lines = data.split('\n')
            for line in lines:
                line = line.strip()
                if line.isdigit() and len(line) > 3:
                    secret = line
                    print(f"Round {round_num}: Secret found (fallback): {secret}")
                    s.send((secret + '\n').encode())
                    round_num += 1
                    data = data.split("What's the secret?:", 1)[-1]
                    break
    
    s.close()

if __name__ == "__main__":
    solve()