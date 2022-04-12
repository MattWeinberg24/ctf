# slightly edited version of solution from
# https://reversingfun.com/posts/picoctf-2021-forensics/

import sys
import struct

with open(sys.argv[1], 'rb') as f:
	buffer = bytearray(f.read())

size = 2893400 # size retrieved from exiftool
width = (1134*3) + (1134%4) # 3-bytes per pixel plus row-padding
height = size // width

st = struct.Struct('<I') # unsigned integer format
st.pack_into(buffer, 0x0A, 54)	# Fix pixel array offset
st.pack_into(buffer, 0x0E, 40)	# Fix DIB Header size
st.pack_into(buffer, 0x16, height)	# Fix image Height property

with open(sys.argv[1] + "_fixed.bmp", 'wb') as f:
	f.write(buffer)

print('File', f.name, 'successfully created')