import math

class Data:
    def __init__(self, date_str):
        self.date_str = date_str

    def get_day(self, month):
        return 28 + (month + math.floor(month / 8)) % 2 + 2 % month + 2 * math.floor(1 / month)

    @classmethod
    def get_day_month_year(cls, date_str):
        try:
            ls = []
            obj_data = cls(date_str)
            for date_part in obj_data.date_str.split("-"):
                ls.append(int(date_part))

            return Data.chek_date(obj_data, *ls)
        except ValueError:
            return (f"Ошибка в формате даты, {date_part} не число")

    @staticmethod
    def chek_date(self, day, month, year):
        if 1 <= month <= 12:
            if 1 <= day <= self.get_day(month):
                if 1900 <= year <= 30000:
                    return f"{day}-{month}-{year} корректна"
                else:
                    return f"Ошибка.Год {year} в дате не корректен"
            else:
                return f"Ошибка. Дата {day} вышла за пределы допустимого значения"
        else:
            return f"Ошибка! В году только 12 месяцев а не {month}"


date_str = input("Введит дату в заданом формате dd-mm-yyyy: ")

print(Data.get_day_month_year(date_str))
