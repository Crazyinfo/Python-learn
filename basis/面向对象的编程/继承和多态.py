class Animals():
    def run(self):
        print('Animal is running......')

bn = Animals()
bn.run()


class Dog(Animals): # 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。
    pass

class Cat(Animals): # 子类获得了父类的全部功能,即cat和dog这两个子类继承了Animals的所有功能
    pass

# 如run的功能:
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 也可以给子类增加一些方法：
class Pig(Animals):

    def run(self):
        print('Pig is running.....')

    def eat(self):
        print('Pig is eating......')

pig = Pig()
pig.run()   # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run(),即继承的另一个好处:多态。
pig.eat()

print(isinstance(pig,Pig))
print(isinstance(pig,Animals))
print(isinstance(bn,Pig))
# 即继承与多态，继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行