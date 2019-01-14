def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1,2,3,4))

# 当不需要立即求和时
# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4)
print(f)
print(f(),"\n")




# 闭包
# why f1(),f2(),f3()returns9,9,9rather than 1,4,9?
def count():
    fs = []
    for i in range(1, 4): # 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
        def f():
             return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count() #输出的f1,f2,f3均为9
print(f1())
print(f2())
print(f3())


# fix:解决以上问题的方法
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

