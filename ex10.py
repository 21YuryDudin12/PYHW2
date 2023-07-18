n = int(input("Введите число монет "))
if n == 1:
    print('Монеты переворачивать не нужно')
else:
    count_1 = 0
    count_0 = 0
    for i in range(n):
        v = int(input("Введите 1, если орел, 0, если решка "))
        if v == 0:
            count_0 +=1
        elif v == 1:
            count_1 +=1
        else:
            print('неверное значение аргумента!!! ')
    count_res = 0
    if count_1 < count_0:
        count_res = count_1
    else:
        count_res = count_0
    print('Минимальное число монет равно: ', count_res)

    
