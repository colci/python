winter_month = ["зиму", 12, 1, 2]
spring_month = ["весну", 3, 4, 5]
summer_month = ["лето", 6, 7, 8]
autumn_month = ["осень", 9, 10, 11]

while True:
    try:
        answer = int(input("Введите число месяца: "))
        if 1 <= answer <= 12:
            break
        else:
            print("Ошибка. Не правильно ввели месяц")
    except ValueError:
        print("Ошибка! Вы вели не число")

if winter_month.count(answer) > 0:
    print(f"Вы выбрали {winter_month[0]}")
elif spring_month.count(answer) > 0:
    print(f"Вы выбрали {spring_month[0]}")
elif summer_month.count(answer) > 0:
    print(f"Вы выбрали {spring_month[0]}")
elif autumn_month.count(answer) > 0:
    print(f"Вы выбрали {autumn_month[0]}")
