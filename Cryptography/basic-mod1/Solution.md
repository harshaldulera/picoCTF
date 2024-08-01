Given message:
```
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213
```

We are told to mod each number by 37 and map the character set as 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

So the result after mod 37 is: 
```
17 26 20 13 3 36 13 36 17 26 20 13 3 36 0 3 3 27 33 4 2 28
```

Now let's map this according to the character set.

```py
char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

numbers = [17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 0, 3, 3, 27, 33, 4, 2, 28]

result = ''.join([char_set[number] for number in numbers])

print(result)
```

Flag:
```
picoCTF{R0UND_N_R0UND_ADD17EC2}
```