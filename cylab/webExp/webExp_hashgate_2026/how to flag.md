## Category
Web Explolation

## Topic
Authentication / Authorization  - Obscurity
Insecure Direct Object Reference (IDOR)

## Vulnerability
The vulnerability is Insecure Direct Object Reference (IDOR). The application used the MD5 hash of a user's numeric ID (for example, 3000 → e93028bdc1aacdfb3687181f2031765d) as the identifier in the profile URL. However, hashing the ID did not enforce authorization—it only obscured the value. Because user IDs were predictable and the server did not verify whether the authenticated user was allowed to access the requested profile, an attacker could generate the MD5 hashes for other user IDs and retrieve their profiles.

## Exploit
The exploit involved recognizing that the application generated profile URLs using MD5(user_id) and that the challenge hinted there were only 20 users, with the current user's ID being 3000. By writing a script to compute the MD5 hash of each candidate ID in the likely range (around 3000–3019), requesting each corresponding profile URL, and checking the responses, it was possible to enumerate valid users. One of the discovered profiles belonged to a higher-privileged user and revealed the flag, demonstrating that the application relied on obscured identifiers instead of proper access control.

Use the solve.py and enter the start and end id after the script ends, look in the flag.txt which was created

=> picoCTF{id0r_unl0ck_69c48f4b}