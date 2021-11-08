import numpy as np

#x1,y1 = input("Quali sono le coordinate di u?")
#x2,y2 = input("Quali sono le coordinate di v?")

def d(u,v):
    x1=u[0]
    y1=u[1]
    x2=v[0]
    y2=v[1]
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

u=(3,0)
v=(0,4)
d=d(u,v)
print(d)