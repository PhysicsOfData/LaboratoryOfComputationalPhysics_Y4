a = [i for i in range(1,100)]

terne=[(i,j,k) for i in a for j in a for k in a if(i<j<k and i**2 + j**2 == k**2)]
terne2=[]

for t in terne:
    div=2
    flag=True

    while(flag and div<t[0]/2):
        if(t[0]%div==0 and t[1]%div==0):
            terne2.append(t)
            flag=False
        div+=1

terneprime=[i for i in terne if i not in terne2]

print(terneprime)
print(len(terneprime))