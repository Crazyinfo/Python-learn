d = {'a': 1,'b': 2,'c': 2}
for m in d:
    print(m)
for n in d.values():
    print(n)
for x,y in d.items():
    print(x,y)

from collections import Iterable
h = isinstance(1233,Iterable) #判断一个对象是否可以迭代
print(h)

for m,n in enumerate([1,2,3,4]):
    print(m,n)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)