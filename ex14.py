n = int(input("Введите число n, программа выведет все степени числа 2 до n: "))
i = 1
print(i)
while i < n:
    i = i*2
    if i < n:
        print(i)
    else:
        break
