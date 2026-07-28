## Category
Web Exploitation

## Topic
Request Late Limitation

## Vulnerability
The system trust the header XFF. The application tracked failed login attempts based on the client IP address, but it accepted the X-Forwarded-For value directly from incoming requests without verifying that it had been added by a trusted reverse proxy

## Exploit
We made a script which loops in the passwords, as well as the ips like 10.0.0.1, 10.0.0.2,...
The correct one, we run the curl request and extract the flag

=>  picoCTF{xff_byp4ss_brut3_1c447e47}