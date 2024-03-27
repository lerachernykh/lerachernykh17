def main1():
    import random
    n = list(random.randint(1,10) for i in range(5))
    v = int(input('введите любое число: '))
    print(n)
    print(v)
    if v in n:
        print ('Поздравляю, Вы угадали число!')
    else:
        print ('Нет такого числа!')
main1()

def main3():
    a = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    dn = tuple(a)
    v = int(input("сколько выходных ты хочешь? "))
    week = a[-v:]
    work = a[:-v]
    print ('Ваши выходные дни: ', week)
    print ('Ваши рабочие дни: ', work)
main3()

def main2():
    import random
    num = list(random.randint(1,10) for i in range(5))
    print(num)
    for n in num:
        if num.count(n)>1:
            print('Повторяющееся число: ',n)
main2()
