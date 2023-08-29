# vault-door-1

## Step 1
Take the code from `checkPassword()` and strip away unnecessary portions. Pad single-digit numbers with zeroes.
```
00  == 'd' 
29 == '3' 
04  == 'r' 
02  == '5' 
23 == 'r' 
03  == 'c' 
17 == '4' 
01  == '3' 
07  == 'b' 
10 == '_' 
05  == '4' 
09  == '3' 
11 == 't' 
15 == 'c' 
08  == 'l' 
12 == 'H' 
20 == 'c' 
14 == '_' 
06  == 'm' 
24 == '5' 
18 == 'r' 
13 == '3' 
19 == '4' 
21 == 'T' 
16 == 'H' 
27 == 'f' 
30 == 'b' 
25 == '_' 
22 == '3' 
28 == '6' 
26 == 'f' 
31 == '0'
```

## Step 2
Sort alphabetically using an online tool such as https://miniwebtool.com/sort-lines-alphabetically/
```
00  == 'd' 
01  == '3' 
02  == '5' 
03  == 'c' 
04  == 'r' 
05  == '4' 
06  == 'm' 
07  == 'b' 
08  == 'l' 
09  == '3' 
10 == '_' 
11 == 't' 
12 == 'H' 
13 == '3' 
14 == '_' 
15 == 'c' 
16 == 'H' 
17 == '4' 
18 == 'r' 
19 == '4' 
20 == 'c' 
21 == 'T' 
22 == '3' 
23 == 'r' 
24 == '5' 
25 == '_' 
26 == 'f' 
27 == 'f' 
28 == '6' 
29 == '3' 
30 == 'b' 
31 == '0'
```

## Step 3
Strip away unnecessary portions and combine into single line.
```
d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0
```
The flag is `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}`
