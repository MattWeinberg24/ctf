s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
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
