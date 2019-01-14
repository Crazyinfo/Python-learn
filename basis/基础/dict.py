m = {5 : 1, 9 : 2, 4: 3}

if 1 in m:
    print('Yes')
else:
    print('No')

if 5 in m:
    print('Yes')
else:
    print('No')

m[8] = 4


if 8 in m:
    print(m.items())
else:
    print('No')

