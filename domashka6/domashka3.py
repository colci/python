class Worker:
    def __init__(self,name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name}  {self.surname} {self.position}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


p = Position("Александр", "Викторович", "Программист", 190000, 50000)
print(p.get_full_name())
print(p.get_total_income())
print(p.position)
print(p._income.get("wage"))