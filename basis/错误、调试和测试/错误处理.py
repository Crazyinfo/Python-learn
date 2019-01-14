try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


# 用logging函数记录错误
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。



# 用raise语句抛出错误
class FooError(ValueError):
    pass

def fau(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

fau('0')