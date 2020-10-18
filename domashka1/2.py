a = float(input("Введите растояние начального результат пробежки: "))
b = float(input("Введите запланированое растояние пробежки: "))
i = 1
while True:
    if i == 1:
        print(f"{i} -й день: {a}")
    else:
        print(f"{i} -й день: " + "{0:0.3f}".format(a * 1.1))
        a = a * 1.1
    if a * 1.1 >= b:
        print(f"{i+1} -й день: " + "{0:0.3f}".format(a * 1.1))
        break
    i += 1