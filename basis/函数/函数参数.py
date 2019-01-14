def f1(a,b,c = 0,* args,** kw):
    print('a =',a,'b =',b,'c =',c,'args =',args,'kw =',kw)
    #a，b为位置参数，c为默认参数，args为可变参数，kw为关键字参数

def f2(a,b,c =0,*,d,** kw):
    print('a =',a,'b =',b,'c =',c,'d =',d,'kw =',kw)
    #命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

print(f1(1,2))
print(f1(1,2,3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x = 99))
print(f2(1,2,3,d = 5,x =5))

args = (1,2,3,4)
kw = {'d': 99,'x': '#'}
print(f1(*args,**kw))