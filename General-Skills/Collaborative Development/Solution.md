```
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git branch
  feature/part-1
  feature/part-2
  feature/part-3
* main
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git checkout feature/part-1                          
Switched to branch 'feature/part-1'
                                                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ cat flag.py 
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git checkout feature/part-2
Switched to branch 'feature/part-2'
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ cat flag.py 
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git checkout feature/part-3
Switched to branch 'feature/part-3'
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ cat flag.py 
print("Printing the flag...")

print("w0rk_7ffa0077}")
```

Flag:
```
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ffa0077}
```