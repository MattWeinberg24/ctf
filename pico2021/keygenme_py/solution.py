#============================================================================#
#============================ARCANE CALCULATOR===============================#
#============================================================================#

import hashlib
from cryptography.fernet import Fernet
import base64
import sys

#picoCTF{1n_7h3_|<3y_of_
#picoCTF{1n_7h3_|<3y_of_75fc1081}

# GLOBALS --v
arcane_loop_trial = True
jump_into_full = True
full_version_code = ""

username_trial = "MORTON"
bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial



print(key_part_static1_trial,end="")
order = [4,5,3,6,2,7,1,8]
for n in order:
    print(hashlib.sha256(bUsername_trial).hexdigest()[n], end="")
print("}")
