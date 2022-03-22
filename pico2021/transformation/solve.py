
# ''.join(
#     [
#             chr(
#                 (ord(flag[i]) << 8) + ord(flag[i + 1])
#             ) 
#         for i in range(0, len(flag), 2)
#     ]
# )



# ENCODING
# 1. join together all the characters
# 2. list comprehension
# 3. for every even integer from 0 to len(flag)...
# 4.    get the character value of
# 5.    the ith char ord left shift 8 + i+1th char ord
#       Because a character is 8 bits, left shifting 8 and adding a character only fills the low 8 bits
#       and the high 8 bits (the first character) remain unchanged

# REVERSE
result = ""
enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
for c in enc:
    c1 = chr(ord(c) >> 8) # first character is high 8 bits
    c2 = chr(ord(c) & 0xFF) # second character is low 8 bits
    result += c1 + c2
print(result)
