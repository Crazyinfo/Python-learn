list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print(index, item)
    print(index)
    print(item)

for index, item in enumerate(list1, 1):  # enumerate还可以接收第二个参数，用于指定索引起始值
    print(index, item)

seq = range(5)
print(seq)
print(enumerate(seq))


'''
如果要统计文件的行数，可以这样写：
count = len(open(filepath, 'r').readlines())

这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
可以利用enumerate()：
count = 0
for index, line in enumerate(open(filepath,'r'))： 
    count += 1
'''