# 果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

#  可以修改的实例属性
class Student1():
    def __init__(self, nam, scor):
        self.nam = nam
        self.scor = scor

    def print1(self):
        print('%s : %s' % (self.nam,self.scor))

bm = Student1('yew',99)
print(bm.scor)
bm.scor = 98
print(bm.scor)


# 无法修改的
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.__name,self.__score))

    # 外部代码要获取name和score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 允许外部代码修改score
    def set_score(self, score):
        self.__score = score

bn = Student('YW',96)
print(bn.score)
bm.score = 97 # 修改无用，输出的任为原先定义的score
print(bn.score)