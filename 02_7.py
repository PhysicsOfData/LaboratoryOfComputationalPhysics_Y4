from math import sqrt
def f(x):
    sqrt(1-x**2)
N=100
h = 2/N
I=0

for i in range(1,N+1):
    I += h*f(i)