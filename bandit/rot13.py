s = "Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh"
result = ""
for c in s:
    n = ord(c)
    if n >= 97 and n <= 122:
        offset = n - 97
        new_offset = (offset + 13) % 26
        result += chr(new_offset + 97)
    elif n >= 65 and n <= 90:
        offset = n - 65
        new_offset = (offset + 13) % 26
        result += chr(new_offset + 65)
    else:
        result += c
print(result)
