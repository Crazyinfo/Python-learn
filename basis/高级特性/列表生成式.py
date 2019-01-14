L = [x * x for x in range(10)]
print(L)
M = [x + y for x in 'ABC' for y in 'XYZ']
print(M)

d = {'a': 1,'b': 2,'c':3}
for x,y in d.items():
    print(x,'=',y)#for循环

N = [x +'='+ y for x,y in d.items()]
print(N)
