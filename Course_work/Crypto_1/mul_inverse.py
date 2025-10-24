import numpy as np

def mod_mul_table(n):
    A = np.arange(1, n).reshape(-1, 1) @ np.arange(1, n).reshape(1, -1)
    return A % n

def mul_inverses(n):
    A = mod_mul_table(n)
    return np.argwhere(A == 1) + 1

def mul_inverse_linalg(a, n):
    A = mod_mul_table(n)
    row = A[a - 1]
    b = np.argwhere(row == 1)[0]
    return b + 1

def mul_inverse(a, n):
    for i in range(n):
        if(a*i % n == 1): 
            return i
if __name__ == "__main__":
    n = 11
    N = mod_mul_table(n)
    print(N)

    R = mul_inverses(n)
    print(R)

    b = mul_inverse(11, 29)
    print(b)