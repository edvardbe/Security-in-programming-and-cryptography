def encrypt(x):
    num = (3*x + 11) % 26
    return chr(num + ord('A'))

def decrypt(y):
    num = 9*(y - 11) % 26
    return chr(num + ord('a'))

def crypt_text(text, crypt):
    encrypted = ''
    for char in text:
        encrypted += crypt(char_to_pos(char))
    return encrypted

def char_to_pos(char):
    return ord(char.lower()) - ord('a')

def pos_to_char(pos):
    return chr(pos + ord('a'))
    
def permutations(text, crypt):
    crypted = crypt_text(text, crypt)
    map = dict(zip(text, crypted))
    return map
        

alphabet = "abcdefghijklmnopqrstuvwxyz"
permutation = permutations(alphabet, encrypt)
print(f"\nTask a) e_k permutation '{alphabet}':\n{permutation}")


m = 'alice'
encrypted = crypt_text(m, encrypt)
print(f"\nTask b) Encrypted '{m}':\n{encrypted}")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
permutation = permutations(alphabet, decrypt)
print(f"\nTask c) inverse permutation '{alphabet}':\n{permutation}")

c = 'RBKKXRQ'
decrypted = crypt_text(c, decrypt)
print(f"\nTask d) Decrypted '{c}':\n{decrypted}")


