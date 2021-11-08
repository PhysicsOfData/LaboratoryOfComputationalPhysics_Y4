def derivative(x, delta):
    def f(x):
        return x*(x-1)
    df = (f(x+delta) - f(x)) / delta
    return df

a = derivative(1, 10E-2)
b = derivative(1, 10E-4)
c = derivative(1, 10E-6)
d = derivative(1, 10E-8)
e = derivative(1, 10E-10)
f = derivative(1, 10E-12)
g = derivative(1, 10E-14)
'''numerically unstable'''
print(a,b,c,d,e,f,g)
print(a-b)