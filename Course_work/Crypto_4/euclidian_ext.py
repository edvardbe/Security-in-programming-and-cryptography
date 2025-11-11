def extended_Euclid(a,b):
  if b==0:
    # gcd(a ,0) = a
    # and gcd(a ,0) = 1 * a + 0 * b
    return a , 1 , 0
  else:
    r , q = a % b , a // b
    d , z , w = extended_Euclid(b,r)
    return d , w , z - q * w

if __name__ == "__main__":
  p = 1283
  d_priv = 3
  
  qs = [1307, 1879, 2003, 2027]

  
  for q in qs:
    print(f"-- q-value ({q})-- ")
    phi = (p - 1) * (q - 1)

    # run extended Euclid
    g, x, y = extended_Euclid(d_priv, phi)

    if g != 1:
        print("No modular inverse exists")
    else:
        e = x % phi
        print("Public exponent e =", e)
        print("Check:", (e * d_priv) % phi)