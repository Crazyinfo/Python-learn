# Determine whether an integer is a palindrome. Do this without extra space.


# 自解
def palindrome(x):
    r = int(str(x)[::-1])
    if x == r:
        return x
    else:
        return 'This is not a palindrome'

print(palindrome(12321))
print(palindrome(121))
print(palindrome(21))


def palindrome1(x):
    p, res = x, 0
    while p >= 1:
        res = res * 10 + p % 10
        p = p // 10
    return res == x

print(palindrome1(12321))
print(palindrome1(1232))