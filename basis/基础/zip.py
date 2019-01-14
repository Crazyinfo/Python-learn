a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]

zipped = zip(a,b)     # 打包为元组的列表
print(zipped)
for i in zipped:
    print(i)
print('\n')

print(zip(a,c))      # 元素个数与最短的列表一致
for k in zip(a,c):
    print(k)
print('\n')
print(list(zip(a,c)))
print('\n')


print(zip(*zipped))          # 与 zip 相反，可理解为解压，返回二维矩阵式
for j in zip(*zipped):
    print(j)