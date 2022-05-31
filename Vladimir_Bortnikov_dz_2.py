import random
# Задание 1

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
results = [a,b,c,d,]
for i in results:
    print(i, type(i))
# Задание 2

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list_1):
    if list_1[i].isdigit():
        list_1[i] = list_1[i].zfill(2)
    elif list_1[i].startswith('+'):
        list_1[i] = list_1[i].zfill(3)
    i += 1

n = 1
while n < len(list_1):
    if list_1[n].isdigit() or list_1[n].startswith('+') and list_1[n][1:].isdigit():
        list_1.insert(n, '"')
        list_1.insert(n+2, '"')
        n+=1
    n+=1
print(list_1)
print(' '.join(list_1))

# Задание 4

list_jobs = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in list_jobs:
    print(f'Привет, {el.split()[-1].title()}!')
for el in range(len(list_jobs)):
    list_jobs[el] = list_jobs[el].split()[-1].title() + ' ' + ' '.join(list_jobs[el].split()[:-1])
print(list_jobs)

# Задание 5

cash = [round(random.uniform(0, 1000), 2) for i in range(20)]
print(cash)
for el in cash:
    tmp_num = str(el).split('.')
    if len(tmp_num[-1]) == 1:
        print(f'{tmp_num[0]} руб {tmp_num[-1]}0 коп')
    else:
        print(f'{tmp_num[0]} руб {tmp_num[-1]} коп')
higher = sorted(cash)
lower = sorted(cash, reverse=True)
print(f'Цены отсортированные по возрастанию: {higher}')
print(f'Цены отсортированные по убыванию: {lower}')
print(f'Цены пяти самых дорогих товаров: {lower[:5]}')
