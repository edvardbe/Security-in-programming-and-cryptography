def mul_inverse(a, n):
  for i in range(n):
    if(a*i % n == 1): 
      return i

def verify(c, m, n, e):
  return decrypt(c, n, e) == m

def encrypt(m, n, e):
  return m ** e % n

def decrypt(c, n, d):
  return c ** d % n
  
p = 47
q = 83
e = 3

n = p*q
phi = (p-1)*(q-1)

print(f"-- Task 2 - RSA --")
print(f"1. Private key")
d = mul_inverse(e, phi)
print(f"k_priv (p, q, d): ({p}, {q}, {d})")
print(f"\n2. Verify message")
m = 100
c = 964
isLegit = verify(c, m, n, e)
print(f"Is signature {c} valid for message {m}: {isLegit}")

print(f"\n3. Encrypt message")

n_B = 3127
e_B = 33

c = encrypt(m, n_B, e_B)

print(f"Encrypted message {m} with public key ({n_B}, {e_B}): {c}")


