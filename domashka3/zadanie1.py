def divisionNumber(x, y):
    while True:
        try:
            return x / y
        except ZeroDivisionError:
            print("Ошибка! нельзя делать на 0")


def MenuInput():
    message = ("Введите первое число: ", "Введите второе число: ")
    nums = []
    i = 0
    while i < 2:
        try:
            nums.insert(i, float(input(message[i])))
            i += 1
        except ValueError:
            print("Ошибка вы ввели не число")
    print(divisionNumber(float(nums[0]), float(nums[1])))


MenuInput()