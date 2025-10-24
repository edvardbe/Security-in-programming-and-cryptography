import math
from mul_inverse import mul_inverse
from affine_ciphers import char_to_pos, pos_to_char

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def brute_force_decrypt(cipher):
    results = []
    for a in range(len(alphabet)):
        a_inv = mul_inverse(a, 26)
        if(a_inv == None):
            continue
        for b in range(len(alphabet)):
            res = decrypt_affine(cipher, a_inv, b)
            results.append({
                "key": (a, b),
                "a_inv": a_inv,
                "decrypted": res
            })
    return results

def decrypt_affine(cipher, a_inv, b):
    res = ""
    for char in cipher:
        if ('A' <= char <= 'Z'):
            y = char_to_pos(char)
            x = (a_inv * (y - b)) % 26
            res += pos_to_char(x)
    return res

cipher = "RGMRQ ERQMZ MZXMD ENNZU QFD"

all_decryptions = brute_force_decrypt(cipher)

print(f"Total possible decryptions: {len(all_decryptions)}")
for decryption in all_decryptions:
    print(f"Key (a, b): {decryption['key']}, Decrypted: {decryption['decrypted']}")