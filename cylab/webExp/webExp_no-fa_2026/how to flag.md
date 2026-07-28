## Category 
Web Exploitation

## Topic
2FA and Sessions

## Vulnerability
- The passwords uses the SHA256 but with no salt, meaning the same string will always give the same hash making them easier to crack.
- The otp is being sent in the cookie.

## Exploit
Use sqlite3 to find the users and credentials of the admin, and you can crack the password [here](https://crackstation.net/), then use it to login, after reaching the 2fa, you use the session in the cookie and decode it as a flask session cookie, not the normal jwt to get the otp_secret, you can decode [here](https://www.kirsle.net/wizards/flask-session.cgi)

=> picoCTF{n0_r4t3_n0_4uth_2b765193}