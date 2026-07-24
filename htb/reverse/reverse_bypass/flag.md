┌──(derfeb㉿kali)-[~/…/CTF/htb/reverse/reverse_bypass]
└─$ sudo apt install mono-utils       
monodis --output=bypass.il bypass.exe
cat bypass.il

┌──(derfeb㉿kali)-[~/…/CTF/htb/reverse/reverse_bypass]
└─$ python3 test.py                            
0 'Wrong username and/or password'
1 'Enter a username: '
2 'Enter a password: '
3 'ThisIsAReallyReallySecureKeyButYouCanReadItFromSourceSoItSucks'
4 'Please Enter the secret Key: '
5 'Nice here is the Flag:HTB{'
6 '}'
7 'Wrong Key'
8 'SuP3rC00lFL4g'
9 'This executable has been obfuscated by using RustemSoft Skater .NET Obfuscator Demo version. Please visit RustemSoft.com for more information.'
10 'This executable has been obfuscated by using RustemSoft Skater .NET Obfuscator Demo version. Please visit RustemSoft.com for more information.'
11 'This executable has been obfuscated by using RustemSoft Skater .NET Obfuscator Demo version. Please visit RustemSoft.com for more information.'
12 'This executable has been obfuscated by using RustemSoft Skater .NET Obfuscator Demo version. Please visit RustemSoft.com for more information.'
                                                                                                                                                                                    
┌──(derfeb㉿kali)-[~/…/CTF/htb/reverse/reverse_bypass]
└─$ 

=> HTB{SuP3rC00lFL4g}


```
The core "catch" is a classic client-side trust violation, and it shows up in two layers here:

**1. The auth flow itself is fake/broken by design**
Method `0::1` (the first username/password prompt) reads your input with `Console.ReadLine()` but never actually checks it against anything — it hardcodes the result to `false` (`ldc.i4.0`) and returns. So that whole first prompt is a decoy; no input could ever pass it. That's a small joke/misdirection built into the challenge, separate from the real check.

**2. The real "security" relies on a secret that ships inside the client**
The actual check (`0::2`) compares your input against a hardcoded string (`ThisIsAReallyReallySecureKeyButYouCanReadItFromSourceSoItSucks` — even the string itself mocks this) loaded from the embedded encrypted resource. The catch is *how* that resource is "encrypted":

- The program uses `RijndaelManaged` (AES) properly generates a key and IV size template via `GenerateKey()`/`GenerateIV()`...
- But then it **reads the actual key and IV bytes from the front of the very same file it's decrypting** — `[32-byte key][16-byte IV][ciphertext]`, all sitting together in the one resource blob shipped with the executable.

So the "encryption" provides zero real protection: anyone with the binary already has the key sitting right there in the same file, at a fixed offset, no extraction of runtime secrets or memory needed. It's encryption theater — the padlock and the key are taped to the same box.

That's the whole point of the hint: **"the client is in full control."** Any check, secret, or crypto operation that happens entirely on hardware you own and can inspect isn't actually a barrier — you can always read the plaintext logic and any embedded keys, no matter how it's wrapped, because nothing is happening on a server you don't control. This is the same principle behind why client-side license checks, hardcoded API keys in mobile apps, or "obfuscated" DRM in binaries all eventually fall to reverse engineering — the secret has to live somewhere the attacker can read it.
```