b = int(input("Введите сумму чисел: "))
c = int(input("Введите произведение чисел: "))
a = 1
x1 = 0
x2 = 0
dis = b*b - 4*a*c
if dis  == 0:
    x1 = x2 = -b / 2
if dis < 0:
    x1 = x2 = 0
if dis > 0:
    x1 = (-b + dis**0.5) / 2 * a
    x2 = (-b - dis**0.5) / 2 * a
print (int(x1*-1),int(x2*-1)) 


