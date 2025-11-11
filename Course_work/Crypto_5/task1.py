def pow_sequence(base, n, p):
  print(f"-- Base-{base} powers with p = {p} in range i = 1, ..., {n} --")
  distinct = 0
  for i in range(1, n + 1):
    res = pow(base, i, p)
    if distinct == 0 and res == 1:
      distinct = i
    print(f"{res}", end=" ")
  print(f"\nNumber of distinct residues: {distinct}\n")
  
    
p = 101
n = 100
pow_sequence(3, n, p)

pow_sequence(5, n, p)