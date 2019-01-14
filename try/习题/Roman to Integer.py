# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

"""
1相同的数字连写、所表示的数等于这些数字相加得到的数、如：Ⅲ=3；
2小的数字在大的数字的右边、所表示的数等于这些数字相加得到的数、 如：Ⅷ=8、Ⅻ=12；
3小的数字（限于 I、X 和 C）在大的数字的左边、所表示的数等于大数减小数得到的数、如：Ⅳ=4、Ⅸ=9；
4正常使用时、连写的数字重复不得超过三次；
5在一个数的上面画一条横线、表示这个数扩大 1000 倍。
"""
# 网摘

# 罗马数字采用七个罗马字母作数字
# 更适用,读有加有减的罗马数字应该从右往左读
d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def romanToInt1(s):
    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c
    return res


print(romanToInt1('XII'))
print(romanToInt1('XIX'))



map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def romanToInt(s):
    num, pre = 0, 1000
    for i in [map[j] for j in s]:
        num, pre = num + i - pre*2 if i > pre else num + i, i
    return num

print(romanToInt('XII'))
print(romanToInt('XIX'))




