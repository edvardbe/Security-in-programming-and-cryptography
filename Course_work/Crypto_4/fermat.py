import math

def fermat(n):
  
  if n & 1 == 0:
    return (2, n/2)
  
  a = math.ceil(math.sqrt(n))
  
  if a * a == n:
    return (a, a)
  
  a += 1
  
  for _ in range(n):
    b_squared = a * a - n
    b = math.ceil(math.sqrt(b_squared))
    if b * b == b_squared:
      return (a + b, a - b)
    
    a += 1
  
  return None

n = 275621053
print(fermat(n))