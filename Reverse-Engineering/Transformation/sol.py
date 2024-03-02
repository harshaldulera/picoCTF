encoded = open('enc', encoding='utf-8').read()
flag = ""

for i in range(0, len(encoded)):
    char1 = chr((ord(encoded[i]) >> 8))
    char2 = chr(encoded[i].encode('utf-16be')[-1])
    flag += char1
    flag += char2

print(flag)