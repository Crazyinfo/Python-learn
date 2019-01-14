def adder(x):
    def wrapper(y):
        return x + y
    return wrapper

adder5 = adder(5)
print(adder5)
# 输出 15
print(adder5(10))
# 输出 11
print(adder5(6))
