'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
'''
'''
n,m,k = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')
'''

'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input:     5

Output:  6
'''
days = int(input('Введите количчество дней: '))
# range(6) -> 0, 1, 2, 3, 4
# range(5, 10) -> 5, 6, 7, 8, 9
# range(1, 10, 2) -> 1, 3, 5, 7, 9
count_days = 0
max_temp = 0
for num_day in range(1, days + 1):
    day = int(input(f'Введите темп. в день {num_day}: '))
    if day > 0:
        count_days += 1
    else:
        if count_days > max_temp:
            max_temp = count_days
        count_days = 0

print(max_temp)

count_w = int(input('Введите колисество арбузов: '))
min_w = int(input('Введите вес арбуза: '))
max_w = min_w
for i in range(count_w - 1):
    w = int(input('Введите вес арбуза: '))
    if w > max_w:
        max_w = w
    elif w < min_w:
        min_w = w

print(min_w, max_w)

