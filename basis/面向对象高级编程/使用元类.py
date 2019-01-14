class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()

print(type(Hello))
print(type(h),'\n')
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello




# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self,name = 'world'):
    print('Hello,%s!' % name)

Wosd = type('Hello',(object,),dict(hello = fn)) # 创建Hello class
k = Wosd()
k.hello()
print(type(Wosd))
print(type(k),'\n')

# 要创建一个class对象，type()函数依次传入3个参数：
#   1.class的名称；
#   2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#   3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# 要控制类的创建行为，可以使用metaclass(元类)。
# 先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。