```
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_decode(cipher):
    dec = ""
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        b = ""
        b += "{0:04b}".format(ALPHABET.index(cipher[c]))
        b += "{0:04b}".format(ALPHABET.index(cipher[c + 1]))
        # turn the binary string to a character and add
        dec += chr(int(b, 2))

    # return
    return dec


def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


enc = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

for key in ALPHABET:
    # initialize string
    s = ""

    for i, c in enumerate(enc):
        # unshift it based on key
        s += unshift(c, key[i % len(key)])

    s = b16_decode(s)

    print(s)
```


Flag:
```
picoCTF{et_tu?_07d5c0892c1438d2b32600e83dc2b0e5}
```