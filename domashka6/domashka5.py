class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Рисует {self.title} класса Pen")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисует {self.title} класса Pencil")

class Handle(Stationery):
    def draw(self):
        print(f"Рисует {self.title} класса Handle")

p = Pen("ручка")
p.draw()

pl = Pencil("карандаш")
pl.draw()

h = Handle("маркер")
h.draw()