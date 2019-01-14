# 提问,以下的输出结果是什么
def testFun():
    temp = [lambda x : i*x for i in range(4)]
    return temp

for everyLambda in testFun():
    print(everyLambda(2))

# Python 的闭包的后期绑定导致的 late binding，这意味着在闭包中的变量是在内部函数被调用的时候被查找。
# 所以结果是，当任何 testFun() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找，
# 到那时，无论哪个返回的函数被调用，for 循环都已经完成了，i 最后的值是 3，
# 因此，每个返回的函数 testFun 的值都是 3。因此一个等于 2 的值被传递进以上代码，它们将返回一个值 6 （比如： 3 x 2）。


# 解决方案
'''第一种：创建一个闭包，通过使用默认参数立即绑定它的参数'''

def testFun1():
    temp = [lambda x ,i=i: i*x for i in range(4)]
    return temp

for everyLambda in testFun1():
    print (everyLambda(2))

'''第二种：使用functools.partial 函数，把函数的某些参数（不管有没有默认值）给固定住（也就是相当于设置默认值）'''

from functools import partial
from operator import mul

def testFun2():
    return [partial(mul,i) for i in range(4)]

for everyLambda in testFun2():
    print (everyLambda(2))

'''第三种：优雅的写法，直接用生成器'''

def testFun3():
     return (lambda x ,i=i: i*x for i in range(4))

for everyLambda in testFun3():
    print (everyLambda(2))

'''第四种：利用yield的惰性求值的思想'''

def testFun4():
    for i in range(4):
        yield lambda x : i*x

for everyLambda in testFun4():
    print (everyLambda(2))