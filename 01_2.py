"""this funciton requires as arguments
a list and the number of how many numbers has to be passed"""
def f(alist,x):
    list=[i for i in alist]
    for i in range(x):
        list.append(i)
    return list

alist = [1,2,3]
ans = f(alist,5)
print (ans)
print (alist)