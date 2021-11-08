ans=[(i,j) for i in range(3) for j in range(4)]
print(ans)

# ans1=[]
# ans1 = map(lambda x: x*x, filter(lambda x: x%2 == 0, range(5)))
# print (list(ans1))

a=[x*x for x in range(5) if x%2==0]
print(a)