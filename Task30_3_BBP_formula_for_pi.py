# Формат: 1000
# Точность: 1000 знаков после разделителя

d = int(input('Вывести число Пи со следущим количеством знаков после разделителя: '))
from decimal import Decimal, getcontext
getcontext().prec=d
print (sum(1/Decimal(16)**k *
    (Decimal(4)/(8*k+1) -
    Decimal(2)/(8*k+4) -
    Decimal(1)/(8*k+5) -
    Decimal(1)/(8*k+6)) for k in range(1001)))