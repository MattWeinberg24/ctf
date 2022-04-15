import pikepdf

# iterate over passwords
for n in range(1000000000):
    p = str(n).rjust(9,'0')
    # password = p[0:3] + "-" + p[3:5] + "-" + p[5:9]    

    try:
        # open PDF file
        with pikepdf.open("2021-return-enc.pdf", password=p) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", p)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        print(p)
        continue