# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# 网摘
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = lambda x: (1, -1)[x < 0] # x < 0时sign取值-1，否则取值1
    r = int(str(sign(x) * x)[::-1])
    return (sign(x) * r, 0)[r > 2 ** 31 - 1]


print(reverse(123))
print(reverse(-123))
print(reverse(120))


m = -2
l = (3, 4)[m > 0]
print(l)
