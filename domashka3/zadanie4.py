def getRank(x, y):
    z = x
    for i in range(0, int(y)-1):
        z *= x
    return z


def getRank2(x, y):
    return x ** y


def MenuInput():
    result = [0, 0]
    ls = ("Возведем число x в степень y", "Введите действительное положительное число: ",
          "Введите целое отрицательное число: ")
    print(ls[0])
    i = 1
    while i < len(ls):
        try:
            result.insert(i - 1, float(input(ls[i])))
            if i == 2 and float(result[i-1]) >= -1:
                print("Вы вели не отрицательное число")
                continue
            i += 1
        except ValueError:
            print("Вы ввели не число")

    return result[:2]


x, y = MenuInput()
print(f"Результат возведения в степень {1/getRank(x, abs(y))} и вторым способом {1/getRank2(x, abs(y))}")




