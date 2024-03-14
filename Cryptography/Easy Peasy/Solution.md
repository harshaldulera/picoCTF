Description: A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})

Solution:
```
┌──(kali㉿kali)-[~/Desktop/picoctf]
└─$ python3 easy_peasy.py
[+] Opening connection to mercury.picoctf.net on port 36981: Done
/home/kali/Desktop/picoctf/easy_peasy.py:7: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("This is the encrypted flag!\n")
[*] flag: 5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c
[+] Causing wrap-around: Done
/home/kali/Desktop/picoctf/easy_peasy.py:18: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendlineafter("What data would you like to encrypt? ", "A" * chunk_size)
/home/kali/.local/lib/python3.11/site-packages/pwnlib/tubes/tube.py:841: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
[+] The Flag: b'7f9da29f40499a98db220380a57746a4'
[*] Closed connection to mercury.picoctf.net port 36981
```

Flag: 
```
picoCTF{7f9da29f40499a98db220380a57746a4}
```