monts = {12: "зиму", 1: "зиму", 2: "зиму",
         3: "весну", 4: "весну", 5: "весну",
         6: "лето", 7: "лето", 8: "лето",
         9: "осень", 10: "осень", 11: "осень"}

while True:
    try:
        answer = int(input("Введите число месяца: "))
        if 1 <= answer <= 12:
            print(f"Вы выбрали {monts.get(answer)}")
            break
        else:
            print("Ошибка. Не правильно ввели месяц")
    except ValueError:
        print("Ошибка! Вы вели не число")
