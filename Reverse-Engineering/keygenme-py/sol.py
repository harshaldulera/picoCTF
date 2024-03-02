import hashlib

keys = [4,5,3,6,2,7,1,8]
username = b"FRASER"
userhash = hashlib.sha256(username).hexdigest()

key = ""

for final in keys:
    key += userhash[final-1]

print(key)