def nol():
    print('2018-01-27')

nol()

f = nol

# __name__属性可以获取函数的名字
print(nol.__name__)
print(f.__name__,"\n")

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()