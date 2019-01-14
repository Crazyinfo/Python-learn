# 计算出n阶乘中尾部零的个数
def trailingZeros(n):
    i = 1
    s = 1
    while i <= n:
        s = i * s
        i = i + 1
    return s

bm = trailingZeros(15)
print(bm)

bx = str(bm)
m = 0
for x in bx[::-1]:
    if x == '0':
        m = m + 1
    else:
        break

print(m)