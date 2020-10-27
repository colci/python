class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc_weight(self):
        #исходя из условия задачи для 1го см. покрытия используется 5 кг асфальта
        return round(self._lenght * self._width * 25 * 5/1000, 3)

r = Road(5000, 20)
print(f"Для строительства дороги длиной {r._lenght} м. и шиириной {r._width} м., потребуется {r.calc_weight()}т асфальта.")