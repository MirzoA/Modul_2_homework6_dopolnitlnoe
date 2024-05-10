num = int(input('Введите число от 3 до 20: '))
result = []
if num >= 3 and num <= 20:
    sum_ = 0
    for i in range(1, num):
        for j in range(i, num):
            if i == j:
                continue
            sum_ = i + j
            if num % sum_ == 0:
                result.append(i)
                result.append(j)

    print('Нужный пароль для', num,': ', result)

else:
    print('Вы ошиблись')
