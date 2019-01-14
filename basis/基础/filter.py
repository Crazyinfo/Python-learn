def is_odd(n):
    return n % 2 == 1

print(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))) #list将Iterator全部输出

def not_empty(s):
    return s and s.strip() #将一个序列中空字符串删除

print(list(filter(not_empty,['A','B','',None,'C',' '])),"\n")

#filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
