```py
from decimal import *
from tqdm import tqdm

N = Decimal(16157656843214630540782260519598878842336783177348929017407633211352136367960754624019502746024050951385898980874283377584450132814889668660733557107718646717269919187065580712312669764271846738002>
e = Decimal(3)
c = Decimal(12200123185888718861325247578988844221745345580555937133090883049102739910735547326599771339806853708992578501219708124057007937105466740621542375448401776167468056686663174811408726056537684848672>


def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:-1]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii


# Find padding
getcontext().prec = 280  # Increase precision
padding = 0
for k in tqdm(range(0, 10_000)):
    m = pow(k * N + c, 1 / e)

    m_ascii = int_to_ascii(m)

    if "pico" in m_ascii:
        padding = k
        break

print("Padding: %s" % padding)

# Increase precision further to get entire flag
getcontext().prec = 700

m = pow(padding * N + c, 1 / e)
m_ascii = int_to_ascii(m)
print("Flag: %s" % m_ascii.strip())
```

Flag:
```
picoCTF{e_sh0u1d_b3_lArg3r_0b39bbb1}
```