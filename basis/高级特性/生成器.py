L = [x * x for x in range(10)]
print(L,"\n")

g = (x * x for x in range(10)) #把[]改成()即是创建生成器generator()的一种方法
print(g)
print(next(g))#一个一个输出
for y in g:
    print(y) #遇到genertor一般不用next，用for循环来迭代
print("\n")

def fibb(ma):
    n,a,b = 0,0,1
    while n < ma:
        print(b)
        t = (b,a + b)
        a = t[0]
        b = t[1]
        n = n + 1
fibb(10)
print("\n")


def fib(max):
    m,g,q = 0,0,1
    while m < max:
        yield q #一个函数中包含yield关键字，这个函数即是一个genertor
        t = (q,g + q)
        g = t[0]
        q = t[1]
        m = m + 1
print(next(fib(6)))
print("\n")

def odd():
    print("step 1")
    yield 1
    print('steo 2')
    yield 3
    print('step 2')
    yield 5
print(next(odd()))   #执行过程中遇到yield就中断