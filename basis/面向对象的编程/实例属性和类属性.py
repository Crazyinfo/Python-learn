class Student1(object):
    def __init__(self,name):
        self.name = name

s = Student1('Bob')
s.score = 90
print(s.score)


# 直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student2(object):
    name = 'Student'

s = Student2() # 创建实例s
print(Student2.name)
print(s.name)
s.name = 'Mahil' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student2.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
