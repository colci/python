class Cell:
    def __init__(self,cell):
        self.cell = int(cell)


    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if (self.cell > other.cell):
            return self.cell - other.cell
        else:
            return "Ошибка! Разность количества ячеек двух клеток не больше нуля"


    def __str__(self):
        return f"{round(self.cell)}"

    def __mul__(self, other):
        return self.cell * other.cell


    def __truediv__(self, other):
        if other.cell > 0:
            return round(self.cell / other.cell)
        else:
            return "Ошибка! Ячейки клетки деляться на ноль клеток"



    def make_order(self):
        result = ""
        for i in range(self.cell):
            if (i % 5 == 0 and i != 0):
                result = result + "\n"

            result = result + "@"
        return result
c = Cell(12)
c2 = Cell(7)
print(f"Первая клетка имеет {c} клеток")
print(f"Вторая клетка имеет {c2} клеток")
print(f"Объединение двух клеток {c + c2}")
print(f"Разность двух клеток {c - c2}")
print(f"Результат деления двух клеток {c / c2}")
print(c.make_order())
