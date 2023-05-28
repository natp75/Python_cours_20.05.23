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


