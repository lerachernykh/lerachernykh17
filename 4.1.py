def z1(a):
    return a % 7 == 0
print (z1(3))

def z3(a):
    d, m, y = map(int, a.split('.'))
    if d * m == int(str(y)[-2:]):
        return True
    else:
        return False
print (z3('02.11.2022'))

def z4(n):
    d = list(map(int, n))
    b1 = d[:len(d)//2]
    b2 = d[len(d)//2:]
    sum_b1 = sum(b1)
    sum_b2 = sum(b2)
    if sum_b1 == sum_b2:
        return True
    else:
        return False
print (z4('385916'))

