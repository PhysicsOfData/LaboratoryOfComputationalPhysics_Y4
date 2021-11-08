import sys
sys.float_info
from math import inf
under = 1.0
over = 1.0
flag = True

while(flag):
    old_u = under
    under = under/2
    if(under==0):
        print(f'overflow reached is {old_u}')
        flag=False

flag=True

while(flag):
    old_o = over
    over = over * 2
    if(over==inf):
        print(f'underflow reached is {old_o}')
        flag=False