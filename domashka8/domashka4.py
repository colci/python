class Store:
    def __init__(self):
        pass

class OfficeEquipment:
    def __init__(self, name, model):
        self._name = name
        self._model = model

class Printer(OfficeEquipment):
    def __init__(self, name,model, speed_printing, color_printing):
        super().__init__(name, model)
        self._speed_printing = speed_printing
        self._color_printing = color_printing

class Scanner(OfficeEquipment):
    def __init__(self, name, model, speed_scaning):
        super().__init__(name, model)
        self._speed_scaning = speed_scaning

class Xerox(OfficeEquipment):
    def __init__(self, name, model, duplex_scaning, speed):
        super().__init__(name, model)
        self._duplex_scaning = duplex_scaning
        self._speed = speed

    def test(self):
        print(f"{self._speed} {super()._name}")

m = Xerox("Epson", "cx4300", True, 35)
m.test()