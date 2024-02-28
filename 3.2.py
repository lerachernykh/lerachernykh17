a = []
while True:
    a.append(input('введите слово: '))
    if input() == 'стоп':
        break
b = ' '.join(a)
print(b)