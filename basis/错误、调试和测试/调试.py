# 第一种方法将错误打印出来，用print()
# 第二种方法，凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
def foo(s):
    n = int(s)
    assert n != 0,'n is zero' # ssert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10 / n

def  main():
    foo('0')

if __name__ == '__main__':
    main()

# 第三种方法，把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件。
import logging

x = '0'
y = int(x)
logging.info('y = %d' % y)
print(10 / y)

import logging
logging.basicConfig(level=logging.INFO)
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。



# 第四种方法是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
import pdb

k = '0'
g = int(k)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / g)
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行