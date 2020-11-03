from abc import ABC, abstractmethod
class Сlothes(ABC):
    @property
    @abstractmethod
    def calc_fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.calc_fabric_consumption + other.calc_fabric_consumption


class Coat(Сlothes):
    def __init__(self, V):
        self.V = V

    @property
    def calc_fabric_consumption(self):
        print(f"Для пошива пальто требуется {round(self.V / 6.5 + 0.5, 2)} ткани")
        return round(self.V / 6.5 + 0.5, 2)

class Suit(Сlothes):
    def __init__(self, H):
        self.H = H

    @property
    def calc_fabric_consumption(self):
        print(f"Для пошива платья теребуется {round(self.H * 2 + 0.3, 2)} ткани")
        return round(self.H * 2 + 0.3, 2)
c = Coat(54)
s = Suit(1.8)

print(f"Общий расход ткани {c + s}")
