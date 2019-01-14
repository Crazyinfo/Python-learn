class Animals():
    def run(self):
        print('Animal is running......')

a = Animals()

# type 判断类型
print(type(123))
print(type(abs))
print(type(a))
print(type(123)==type(353))
print(type(123)==int)

# isinstance 判断类型
print(isinstance(a,Animals))
print(isinstance([1,2,3],(tuple,list))) # 还可以判断一个变量是否是某些类型中的一种

# 在tyoe和isinstance中总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# dir 获得一个对象的所有属性和方法
print(dir('abc'),"\n")
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法



# 配合getattr()、setattr()以及hasattr()，可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
# 紧接着，可以测试该对象的属性：
print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'
