import random
import enchant
'''
This is a small and simple demonstration for the Caesar Cypher. It can encrypt with an optional offset, 
decrypt with an offset or simply brute force decrypt. The brute force method involves
making the input a list by tokenizing it by spaces, then 
'''
letter_num_pairs = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
num_letter_pairs = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def encrypt(input,offset=-1):
    if(offset==-1):
        offset=random.randint(1,25)
    input=input.lower()
    encrypted_str = ""
    for char in input:
        if (char.isalpha()):
            num = letter_num_pairs[char]
            offset_num = (num + offset) % 25
            encrypted_str += num_letter_pairs[offset_num]
        else:
            encrypted_str += char
    return encrypted_str

def decrypt(encrypted:str,offset):
    decrypted_str = ""
    for char in encrypted:
        if (char.isalpha()):
            num = letter_num_pairs[char]
            offset_num = (num - offset) % 25
            decrypted_str += num_letter_pairs[offset_num]
        else:
            decrypted_str += char
    return decrypted_str

def brute_force_decrypt(encrypted:str):
    '''What this function will do is that it will try to find words that belong to the English dictionary and if so it will'''
    en_dict =enchant.Dict("en_US")
    for i in range(0,26):
        possible_decrypt = decrypt(encrypted,i)
        possible_decrypt=' '.join(possible_decrypt.split())
        possible_decrypt_lst = possible_decrypt.split(" ")
        num_elements= len(possible_decrypt_lst)
        #print(possible_decrypt_lst)
        decrypted_str = ""
        strikes = 0
        for j in range(0,num_elements):
            if(strikes>2):
                continue
            elif(strikes<-2):
               decrypted_str=possible_decrypt
            elif(len(possible_decrypt_lst[j])==1):
                continue
            elif(en_dict.check(possible_decrypt_lst[j])):
                decrypted_str += possible_decrypt_lst[j]
                decrypted_str += " "
                #print("accepted",possible_decrypt_lst[j])
                strikes -= 1
            else:
                strikes += 1
        if(0>strikes):
            print(decrypted_str)
            break








encrypted = encrypt("This is a secret and encoded message classified ")
print("Encrypted string = ",encrypted)
brute_force_decrypt(encrypted)
