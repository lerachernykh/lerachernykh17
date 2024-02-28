n = int(input('введите кол-во слов: '))
a = []
for i in range(n):
    a.append(input('введите слово: '))
b = ' '.join(a)
print(b)