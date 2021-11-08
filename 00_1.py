
num=[]
for i in range (1,101):
    if(i%3==0 and i%5==0):
        num.append("MickeyMouse")
    elif(i%3==0):
        num.append("Mickey")
    elif(i%5==0):
        num.append("Mouse")
    else:
        num.append(i)

j=0
while(j<len(num)):
    if(num[j]=="Mickey"):
        num[j]="Donald"
    elif(num[j]=="Mouse"):
        num[j]="Duck"
    j+=1

tupla=()
k=0
while(k<len(num)):
    tupla= tupla + (num[k],)
    k+=1
print(tupla)