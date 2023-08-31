# vault-door-4
# convert ascii values in decimal, hex, and octal, to characters

result = []

ascii = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98]
result += [chr(a) for a in ascii]

hex = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
result += [chr(h) for h in hex]

octal = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o143, 0o61]
result += [chr(o) for o in octal]

char = ['9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e']
result += char

flag = "picoCTF{" + "".join(result) + "}"

print(flag)
