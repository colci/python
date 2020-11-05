class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text

while True:
    try:
        num1 = float(input("Введите делимое число: "))
        num2 = float(input("Введите делитель: "))
        if num2 == 0:
            raise MyZeroDivisionError("Ошибка. Делить на 0 нельзя ")
        print(f"{num1}/{num2} = {round(num1/num2,2)}")
        break
    except ValueError:
        print("Вы вели не число")
    except MyZeroDivisionError as erorr:
        print(f"{erorr}")