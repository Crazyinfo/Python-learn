from collections import Iterable
print(isinstance([],Iterable)) #判断一个对象是否为可迭代对象(可以用for循环的对象统称为:Iterable)
print(isinstance('ABCS',Iterable),"\n")

from collections import Iterator #可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
print(isinstance([],Iterator)) #判断一个对象是否为迭代器
print(isinstance(iter([]),Iterator),"\n") #iter()函数可将可迭代对象变为迭代器
#list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

print(isinstance((x for x in range(6)),Iterator),"\n") #生成器都是Iterator