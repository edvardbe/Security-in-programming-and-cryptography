from euclidian_ext import extended_Euclid

def mod_exp(m, e, n):
  result = 1
  m = m % n
  while e > 0:
    if e & 1:
      result = (result * m) % n
    m = (m * m) % n
    e >>= 1
  return result


p = 1283
q = 2027
n = p * q
d = 3
phi = (p-1)*(q-1)

_, x, _ = extended_Euclid(d, phi)
e = x % phi

# Encrypt message
m = 111
c = mod_exp(m, e, n)

print("Public key (n, e):", (n, e))
print("Ciphertext:", c)