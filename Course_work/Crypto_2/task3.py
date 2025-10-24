from aes_decrypt import bytes2matrix, matrix2bytes, add_round_key, sub_bytes, inv_mix_columns, inv_shift_rows, s_box, inv_s_box, decrypt

# Structure of AES
matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print("-- Structure of AES --\n")
print(matrix2bytes(matrix), "\n")

# Round Keys
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

print("-- Round Keys --\n")
print(matrix2bytes(add_round_key(state, round_key)), "\n")

# Confusion through Substitution
state = [
    [251, 64, 182, 81],
    [146, 168, 33, 80],
    [199, 159, 195, 24],
    [64, 80, 182, 255],
]

print("-- Confusion through Substitution --\n")
print(matrix2bytes(sub_bytes(state, inv_s_box)), "\n")

# Diffusion through Permutation
state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

inv_mix_columns(state)
inv_shift_rows(state)
print("-- Diffusion through Permutation --\n")
print(matrix2bytes(state), "\n")

# Bring it All together
key        = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'

print("-- Bring It All Together --\n")
print(decrypt(key, ciphertext), "\n")