from itertools import cycle
from random import random
from itertools import count
from sys import argv

script_name, start_number = argv

if start_number.isdigit():
    if int(start_number) <= 1000:
        num = cycle([int(random_num) for n in range(50) for random_num in [random() * (100 - int(start_number)) + int(start_number)]])
        i = 0
        print(i)
        while i < 50 and num != 90:
            print(next(num))
            i += 1
        if (num == 90):
            print(num)
else:
    print("Ошибка! Вы ввели не число")
