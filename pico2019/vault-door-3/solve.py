s = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"

result = [""]*32

for i in range(8):
    result[i] = s[i]
for i in range(8,16):
    result[23 - i] = s[i]
for i in range(16,32,2):
    result[46 - i] = s[i]
for i in range(17,32,2):
    result[i] = s[i]

result = "picoCTF{" + ''.join(result) + '}'
print(result)