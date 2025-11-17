p = 97
g = 5
x = 13

print(f"-- Task 2 --")
print(f"\n1. Compute the public key k = g^x mod p")
k = pow(g, x, p)
print(f"k = {g}^{x} mod {p} = {k}")
print(f"Public key: (p = {p}, g = {g}, k = {k})")

m = 42
y = 19

print(f"\n2. Encrypt the message m = 42 using the ephemeral key y = 19 to obtain the ciphertext (c1, c2)")
c1 = pow(g, y, p)
print(f"c1 = g^y mod p: {g}^{y} mod {p} = {c1}")

c2 = (m * pow(k, y, p)) % p
print(f"c2 = m * k^y mod p: {m} * {k}^{y} mod {p} = {c2}")
print(f"Ciphertext: (c1 = {c1}, c2 = {c2})")


print(f"\n3. Decrypt the ciphertext using the private key x = 13.")

def mul_inverse(a, n):
  for i in range(1, n):
    if(a*i % n == 1): 
      return i

s = pow(c1, x, p)
print(f"s = c1^x mod p: {c1}^{x} mod {p} = {s}")

s_inverse = mul_inverse(s, p)
proof = s * s_inverse % p
print(f"s^-1 = {s_inverse} where s * s^-1 mod p = 1: {s} * {s_inverse} mod {p} = {proof}")

m_d = (c2 * s_inverse) % p

print(f"m_d = c2 * s^-1 mod p: {c2} * {s_inverse} mod {p} = {m_d}")  

print(f"\n4. When recovering m, compute the modular inverse using the Extended Euclidean Algorithm and show all steps.")

def extended_Euclid_verbose(a, b, depth=0):
    indent = " " * depth
    if b == 0:
        print(f"{indent}Base case: gcd={a}, coefficients (1,0)")
        return a, 1, 0

    r, q = a % b, a // b
    
    print(f"{indent}Compute: a={a}, b={b}, q={q}, r={r}")
    
    d, z, w = extended_Euclid_verbose(b, r, depth + 1)
    v = z - q * w
    
    print(f"{indent}Backtrack: gcd={d}, w={w}, z - q * w={v}  (check: {w}*{a} + {v}*{b} = {w*a + v*b})")
    
    return d, w, v

_, m_inverse, _ = extended_Euclid_verbose(m, p)

proof = m * m_inverse % p

print(f"\nm^-1 = {m_inverse} where m * m^-1 mod p = 1: {m} * {m_inverse} mod {p} = {proof}")

n = 2

c2_tampered = c2 * n * m_inverse

print(f"c2_tampered = c2 * n * m_inverse: {c2} * {n} * {m_inverse} = {c2_tampered}")

m_d = (c2_tampered * s_inverse) % p

print(f"m_d = c2_tampered * s^-1 mod p: {c2_tampered} * {s_inverse} mod {p} = {m_d}")