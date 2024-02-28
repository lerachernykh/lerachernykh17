import random
a, b = 0, 0
while b != 3:
    c1 = random.randint(1, 10)
    c2 = random.randint(1, 10)
    print(c1, '+', c2, '=... ')
    d = int(input())
    if c1 + c2 == d:
        a += 1
        print('правильно!')
    else:
        b += 1
        print('ответ неверный')
print('игра окончена. верных ответов: ', a)