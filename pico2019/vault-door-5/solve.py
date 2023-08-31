# vault-door-5

from base64 import b64decode
from urllib.parse import unquote

s = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2"

# base64 decode
s = b64decode(s)

# url decode
s = unquote(s)

flag = "picoCTF{" + s + "}"
print(flag)