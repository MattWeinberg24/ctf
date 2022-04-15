# MetaCTF 2021: I Hate Python (Reverse Engineering)

## Description

I hate Python, and now you will too. Find the password.

```
import random

def do_thing(a, b):
	return ((a << 1) & b) ^ ((a << 1) | b)

x = input("What's the password? ")

if len(x) != 25:
	print("WRONG!!!!!")
else:
	random.seed(997)
	k = [random.randint(0, 256) for _ in range(len(x))]
	a = { b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(x), k) }
	b = list(range(len(x)))
	random.shuffle(b)
	c = [a[i] for i in b[::-1]]
	kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]
	valid = len(list(filter(lambda s: kn[s[0]] == s[1], enumerate(c))))

if valid == len(x):
	print("Password is correct! Flag:", x)
else:
	print("WRONG!!!!!!")
```

Near the end of the script there is a comparison checking if valid is equal to the length of the password. This comparison led me to believe that each correct character in the password will add one to valid. By adding a print statement to check the value of valid and sending the program the password MetaCTFAAAAAAAAAAAAAAAAAA I was able to see that my hunch was correct.

Now I can modify the script to brute force each character in the password to find the right password.

```
import random
from os import system

def do_thing(a, b):
	return ((a << 1) & b) ^ ((a << 1) | b)

def python_sucks(passwd, current_length):
	random.seed(997)
	k = [random.randint(0, 256) for _ in range(len(passwd))]
	a = { b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(passwd), k) }
	b = list(range(len(passwd)))
	random.shuffle(b)
	c = [a[i] for i in b[::-1]]
	kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]
	valid = len(list(filter(lambda s: kn[s[0]] == s[1], enumerate(c))))

	if valid > current_length:
		return True
	else:
		return False


currFlag = ''

for i in range(25):
	for j in range(33, 128):
		nextFlag = currFlag + chr(j) + 'A'*(24-i)
		assert(len(nextFlag) == 25)

		if python_sucks(nextFlag, len(currFlag)):
			currFlag = currFlag + chr(j)
			print(currFlag)
			break
```

Flag: gigem{b3_car3ful_b3for3_y0u_c0mmit}
