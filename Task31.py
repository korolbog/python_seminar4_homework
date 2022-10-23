# Задача 31
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

list = []
n = int(input('Введите натуральное число n: '))
x = n
if n > 0:
    if n == 1:
        print(f'{n} = {res}')
    for i in range(2, x+1):
        if x%i == 0:
            count = 0
            while x//i > 0 and x%i == 0:
                x //= i
                count += 1
            list.append(f'{i}^{count}')
    res = str(list)
    res = res.replace("[", "")
    res = res.replace("]", "")
    res = res.replace("',", " *")
    res = res.replace("'", "")
    print(f'{n} = {res}')
else:
    print('Вы ввели неверное число.')




            
            


