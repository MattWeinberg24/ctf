# vault-door-8

## Cleaning up the Java
I cleaned up `VaultDoor8.java` to make it human-readable using whitespace and splitting each statement onto separate lines.

## Unscrambling
Created a new method `unscramble()` that does the same bit swaps as `scramble()` except backwards (hence "reversing" the scramble)

## Getting the flag
I modified the `main()` method to simply unscramble the "expected" scramble defined in `checkPassword()`

Running the file (i.e. `$ java VaultDoor8.java` on command-line) produced the flag "picoCTF{s0m3_m0r3_b1t_sh1fTiNg_89eb3994e}"