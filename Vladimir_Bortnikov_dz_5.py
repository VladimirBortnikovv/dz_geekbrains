#Задание 1
def gen_number(stop, start=0, step=1):
    current = start
    while current < stop:
        yield current
        current += step

n = int(input('Введите число: '))

gen = gen_number(n, 1, 2)

for i in gen:
    print(i)

#Задание 3
def gen_new_list(tutor, klass):
    i = 0
    while i < len(tutor) and i < len(klass):
        yield tutor[i], klass[i]
        i += 1
    while i < len(tutor):
        yield tutor[i], None
        i += 1

tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Анастасия','Юлия'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for i in gen_new_list(tutors, klasses):
    print(i)

#Задание 5
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for number in numbers:
    if numbers.count(number) == 1:
       result.append(number)

print(result)

