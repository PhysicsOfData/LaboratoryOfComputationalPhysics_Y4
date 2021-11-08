from decimal import Decimal

def floaconverter(x): #x deve essere un numero binariodi 32 bits
    bias=127
    s = int(x[0])
    e = str(x[1:9])
    e_dec = int(e, 2)
    i=0
    m=0

    for i in range(23):
        m += int(x[9+i]) * pow(2,-(1+i))

    mantissa = m+1

    f = (-1)**s * mantissa * (pow(2, e_dec - bias))
    return print(m, e_dec, f)
    # return print(len(x))

floaconverter('01000000110101010001111010111000')
floaconverter('11000000100000000000000000000110')