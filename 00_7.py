#con il ciclo for
c1=[]
for i in range(10):
    c1.append(i**3)
print(c1)

#list comprehension
c2=[x**3 for x in range(10)]
print(c2)