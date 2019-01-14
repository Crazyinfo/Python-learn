class Student(object):
    pass

s = Student()
s.name = 'Bob' # # 动态给实例绑定一个属性
print(s.name)

def set_age(self,sge): # 定义一个函数作为实例方法
    self.age = age

Student.age = set_age  # 为了给所有实例都绑定方法，给class绑定方法

s.age = 18
print(s.age)
print(Student.age)
s.score = 99
print(s.score)
print('\n')

class Student1(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称


m = Student1()
m.age = 19
m.name = 'kjskj'
print(m.name,m.age) # 此时无法绑定其他实例


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class MY(Student1):
    pass

MY.score = 99
print(MY.score)
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
