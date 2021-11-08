from numpy import sqrt,sign

def quadsolver(a,b,c):
    x1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    if(x1==x2): 
        return print(f'the two solution are equal: {x1}')
    else:
        return print(f'With standard formula {x1} e {x2} ')

def quadsolver2(a,b,c):
    x1 = (2*c) / (-b - sqrt(b**2 - 4*a*c))
    x2 = (2*c) / (-b + sqrt(b**2 - 4*a*c))
    if(x1==x2): 
        return print(f'the two solution are equal {x1}')
    else:
        return print(f'whith the rewritten formula {x1} e {x2} ')

def quadsolver3(a,b,c):
    x1= (-b-sign(b)*sqrt(b**2-4*a*c))/(2*a)
    x2= c/(a*x1)
    return print(f'whith the stable formula {x1} e {x2} ')


quadsolver(0.001, 1000, 0.001)
quadsolver2(0.001, 1000.0, 0.001)
quadsolver3(0.001, 1000.0, 0.001)

'''il risultato è diverso! Perché?'''