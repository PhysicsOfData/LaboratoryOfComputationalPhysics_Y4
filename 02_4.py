import sys
sys.float_info

flag = True
j = 1.0

while(flag):
    # j = j * 10E-5
    j = j / 1.0000001

    if(j + 1 == 1):
        flag = False
print(j)