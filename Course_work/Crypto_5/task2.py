def mul_inverse(a, n):
    for i in range(n):
        if(a*i % n == 1): 
            return i

def verify(c, m, n, d):
  residue = c**d % n
  print(residue)
  return residue == m


p = 47
q = 83
e = 3

n = p*q
phi = (p-1)*(q-1)

print(f"-- Task 2 - RSA --")
print(f"1. Private key")
d = mul_inverse(e, phi)
print(f"k_priv (p, q, d): ({p}, {q}, {d})")
print(f"2. Verify message")
m = 100
c = 964
isLegit = verify(c, m, n, d)
print(f"Message is legit: {isLegit}")


