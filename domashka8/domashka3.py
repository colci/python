class NotIsDigitalErorr(Exception):
    def __init__(self, text):
        self.text = text

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

print("Заполним список данными типа число.\nДля завершения ввода введите stop")
ls = []
while True:
    try:
        el = input("Введите новое число: ")
        if el.upper() == "STOP":
            print(f"Результат ввода: {ls}")
            break
        if is_digit(el) == False:
            raise NotIsDigitalErorr("Ошибка! Вы вели не число")
        else:
            ls.append(float(el))
    except NotIsDigitalErorr as error:
        print(error)