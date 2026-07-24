
```                                 
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ javac SafeOpener.java                                           
                                                                                                                                                                                     
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ java SafeOpener      
Enter password for the safe: picoCTF{^C                                                                                                                                                                                     
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ 
                                                                                                                                                                                     
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ base64 -d string
base64: string: No such file or directory
                                                                                                                                                                                     
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ base64 -d string.txt
pl3as3_l3t_m3_1nt0_th3_saf3                                                                                                                                                                                     
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ java SafeOpener     
Enter password for the safe: picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
cGljb0NURntwbDNhczNfbDN0X20zXzFudDBfdGgzX3NhZjN9
Password is incorrect

You have  2 attempt(s) left
Enter password for the safe: pl3as3_l3t_m3_1nt0_th3_saf3
cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz
Sesame open
                                                                                                                                                                                     
┌──(derfeb㉿kali)-[~/…/CTF/cylab/reverse/reverse_safe-opener_2022]
└─$ 
```

the string.txt has the string copied from encodedkey, use base64 to decode and get the password