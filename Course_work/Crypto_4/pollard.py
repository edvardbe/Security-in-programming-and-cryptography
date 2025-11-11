from euclidian_ext import extended_Euclid
import math

def pollard(n, B):
  a = 2
  B_factorial = math.factorial(B)
  A = a**B_factorial % n
  
  gcd, _, _ = extended_Euclid(A - 1, n)
  if 1 < gcd < n:
    return gcd
  return None

print("-- Task a) --")

n = 1829
B = 5
f = pollard(n, B)

print(f"Prime factor using Pollard's p - 1: {f}")

print("-- Task b) --")

n = 18779
B = 0
while True:
  B += 1
  f = pollard(n, B)
  if f == None:
    continue
  break

print(f"Prime factor using Pollard's p - 1: {f}, with B = {B}")