On connecting to the nc we get the following output.
```
┌──(kali㉿kali)-[~/Desktop/pico]
└─$ nc saturn.picoctf.net 58984
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
```

Conerting hexadecimal to string
```
chr(0x62) corresponds to 'b'
chr(0x64) corresponds to 'd'
chr(0x61) corresponds to 'a'
chr(0x36) corresponds to '6'
chr(0x38) corresponds to '8'
chr(0x66) corresponds to 'f'
chr(0x37) corresponds to '7'
chr(0x35) corresponds to '5'
```
Flag:
```
picoCTF{gl17ch_m3_n07_bda68f75}
```