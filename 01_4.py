#a usa recursion
"""restituisce il fattoriale di x"""
def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fact(x-1)

print(fact(0))
#b non usa recursion

def fact2(x):
    if(x==0): return 1
    else:
        fact=1
        for i in range(1,x+1):
            fact=i*fact
        return fact

print(fact2(0))