from collections import Counter

file_path = 'cipher.txt'

with open(file_path, 'r') as file:
    cipher = file.read()

english_frequencies = list(" ETAOINSHRLDCUMWFGYPBVKJXQZ")

altered_frequencies = list(" ETNAOSLIRHUGCVYPMBKWXDQFJZ")

dcode_frequencies = list("DI BKCVOQWTSAELYPUMFRGJXHNZ")

bigrams = ["th", "he", "in", "en", "nt", "re", "er", "an", "ti", "es", "on", "at"]

mapping = dict(zip(dcode_frequencies, altered_frequencies))

decrypted = ''.join(mapping.get(ch, ch) for ch in cipher)
print("\nCipher:\n", cipher)
print("\nMapping:\n", mapping)
print("\nDecrypted text:\n")
print(decrypted)