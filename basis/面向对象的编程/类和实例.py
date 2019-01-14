class Student():
    pass

bart = Student()
print(bart) # 0x0000021B57BE6748 运行出的为该地址
print(Student)

bart.name = 'YW' # 给实例绑定一个name属性
print(bart.name,"\n")


class Student1(): # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    def __init__(self, name, score): # 特殊方法“__init__”前后分别有两个下划线！！！
        self.name = name # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        self.score = score

bm = Student1('Yw',99)
print(bm)
print(bm.name)
print(bm.score,"\n")

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。



# 数据封装
class Student3(object):
    def __init__(self, nam, scor):
        self.nam = nam
        self.scor = scor

    def get_grade(self):
        if self.scor >= 90:
            return 'A'
        elif self.scor >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student3('Lisa', 99)
bart = Student3('Bart', 59)
print(lisa.nam, lisa.get_grade())
print(bart.nam, bart.get_grade())