f = lambda x: x * x
print(f(5))

def build(x,y):
    return lambda : x * x + y * y

print(build(3,4))

q = build(3,4)
print(q())