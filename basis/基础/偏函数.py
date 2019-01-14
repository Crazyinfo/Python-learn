print(int('12345'))
print(int('12345',base = 8)) # int()中还有一个参数base，默认为10，可以做进制转换

def int2(x,base=2):
    return int(x,base) # 定义一个方便转化大量二进制的函数

print(int2('11011'))


# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int3：
import functools
int3 = functools.partial(int , base = 2) # 固定了int()函数的关键字参数base
print(int3('11000111'))
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print(int3('110101',base = 8)) # base = 2可以重新定义