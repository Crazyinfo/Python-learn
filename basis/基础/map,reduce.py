#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9]) #map有两个参数，一个是函数，一个是Iterable
print(list(r)) #此处r即为Iterator,list()将其全部输出
print(r)
#以上等同于:
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(n*n)
print(L)

print(list(map(str,[1,2,3,4,5,6,7,8])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#其效果为:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x + y

print(reduce(add,[1,3,5,7,9]))
print("\n")



from functools import reduce
def fn(x,y):
    return x * 10 + y

print(reduce(fn,[1,5,2,9]))
print("\n")


from functools import reduce
DIGITS = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
def str2int(s): #将字符串转化为整数
    def fl(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fl,map(char2num,s))
print(str2int("8797"))


def normalize(str):#将每个单词首字母变为大写
   return str.capitalize()
r=list(map(normalize,['adam', 'LISA', 'barT']))
print(r)