#求素数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter(): #构造一个以3开始的生成器，且为一个无限序列
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n): #筛选函数
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() #初始化序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) #构造新序列

if __name__ == '__main__':
    main()

#也可以用print(main())