class Data:
    def __init__(self, date_str):
        self.date_str = str(date_str)

    @classmethod
    def get_day_month_year(cls, date_str):
        date_list = cls(date_str).date_str.split("-")
        return list(map(int,date_list))
        #.split("-")

date = Data.get_day_month_year("25-12-2020")

print(date)
#dste.get_day_month_year()