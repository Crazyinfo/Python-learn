s = sorted([1,3,2,-31,-3],key = abs,reverse = False) #正向排序，不传入参数reverse时，默认正想排序
print(s)

L = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True) #反向排序
print(L)



def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key = by_name))
print(sorted(L,key = by_score,reverse = True))
print(by_name(L))