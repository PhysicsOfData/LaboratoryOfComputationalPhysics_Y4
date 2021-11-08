import numpy as np
tupla = (1,-1,-5,-8)
"""norma 1"""
def norm(t):
    n=0
    for i in t:
        n += np.abs(i)
    t = t/n
    return t 

"""norma 2"""
def norm2(t):
    n=0
    for i in t:
        n += i**2
    m = np.sqrt(n)
    t=t/m
    return t

print(norm(tupla))
print(norm2(tupla))