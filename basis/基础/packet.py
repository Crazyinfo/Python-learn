def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass #空函数

import math
def quadratic(a, b, c):
    nx = math.sqrt(b*b - 4*a*c)/(2*a)
    ny = -b/(2*a)
    x1 = ny + nx
    x2 = ny - nx
    return x1,x2

print(quadratic(1,-2,1))