Found the flag in the log message of the message.
```
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git log message.py 
commit fadeca9476b6713ec8cdda633aca9e9aebffc698
Author: picoCTF{@sk_th3_1nt3rn_e9957ce1} <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    optimize file size of prod code

commit 2dd46769e2d65656bb14aed0ff5d3237daaa7d9d
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    create top secret project
```

Flag:
```
picoCTF{@sk_th3_1nt3rn_e9957ce1}
```