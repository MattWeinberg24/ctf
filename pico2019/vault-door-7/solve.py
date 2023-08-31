# vault-door-7

int_array = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734291511,
    960049251,
    1681089078
]

# split each integer into four bytes, most significant first (big endian)
bytes_array = [n.to_bytes(4,'big') for n in int_array]

# convert bytes into utf-8
result = [str(b, "utf-8") for b in bytes_array]

flag = "picoCTF{" + "".join(result) + "}"
print(flag)