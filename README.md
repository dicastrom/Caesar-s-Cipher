# Caesar-s-Cipher
This is a small and simple demonstration for the Caesar Cypher. It can encrypt with an optional offset, 
decrypt with an offset or simply brute force decrypt. The brute force method involves
making the input a list by tokenizing it by spaces, then brute forcing each possible offset for the letters and checking
if each letter is part of the english dictionary (can be changed to other languages easily). I allows two strikes for mispelled
words at the beggining of the string but once it can confirm a significant part of the string belongs to the
dictionary it will return the de-coded string.
# Usage= 
<br>
encrypted_string = encrypt(string, optional_offset:int)
<br>
decrypted_str= brute_force_decrypt(encrypted_string)
<br>
Here decrypted_str will hold the original string that was encrypted and encrypted_string will hold the encrypted string.

