# vault-door-3

The entered password `p` is shuffled in the following method and placed into a buffer `b`, where `b_i` is the index of the buffer character and `p_i` is the index of the password character.
* Characters 0 through 7 of the buffer are added as normal (`b[b_i] = p[b_i]`)
* Characters 8 through 15 of the buffer are added via the formula `b[b_i] = p[23 - b_i]`
* Characters 16 through 31 (evens) of the buffer are added via the formula `b[b_i] = p[46 - b_i]`
* Characters 16 through 31 (odds) of the buffer are added as normal (`b[b_i] = p[b_i]`)

These subtractions can be reversed by doing the inverse, where the formula for the second and third loops end up being `p[p_i] = b[23 - p_i]` and `p[p_i] = b[46 - p_i]` respectively, as seen in `solve.py`

Running `solve.py` gives the string `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}`