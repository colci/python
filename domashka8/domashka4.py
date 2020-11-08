import os

class Store:
    def __init__(self):
        self.init_subdivision()
        self.officeEquipment_lib = {}
        self.id = 0
        self.prefix = {1: "xer", 2: "print", 3: "scan"}

    def get_prefix_obj(self,id_prefix):
        return self.prefix.get(id_prefix)

    def get_new_id(self):
        self.id += 1
        return self.id

    def __str__(self):
        result = ""
        for ke, value in self.officeEquipment_lib.items():
            result = result + f"{ke}\n"
            for key, val in value.items():
                result = result + f"   {key}\n"
                for k, val in val.items():
                    result = result + f"      {k} : {val}\n"
        return result;


    def init_subdivision(self):
        self._subdivision = {1: "Приемки", 2: "Отгрузки", 3: "Администрация", 4: "Комплектации"}

    def add_Xerox(self, id_subdiv, name, model, duplex_scaning, speed, count):

        value_subdiv = self.officeEquipment_lib.get(self._subdivision.get(id_subdiv))
        if value_subdiv is None:
            self.officeEquipment_lib.setdefault(self._subdivision.get(id_subdiv), Xerox(name, model, duplex_scaning, speed).get_param_xerox(count))
        else:
            value_xerox = value_subdiv.get(f"xer_{name}_{model}")
            if value_xerox is None:
                self.officeEquipment_lib.setdefault(self._subdivision.get(id_subdiv),
                                                        value_subdiv.setdefault(f"xer_{name}_{model}",
                                                                                 Xerox(name, model, duplex_scaning, speed).get_param_xerox(count)))
            else:
                self.officeEquipment_lib.update({self._subdivision.get(id_subdiv):
                                                    Xerox(name, model, duplex_scaning, speed).get_param_xerox(value_xerox.get("count") + count)})

  #  def get_balance_equipment(self,id_subdiv, id_prefix, name, model)
  #      for el in self.officeEquipment_lib:
   #         el.

    def move_xerox(self, from_id_subdiv, to_id_subdiv, name, model, count):
        value_subdiv = self.officeEquipment_lib.get(self._subdivision.get(from_id_subdiv))
        if value_subdiv is None:
            print(f"В подразделении {self._subdivision.get(from_id_subdiv)}, нет оборудования {name} {model}")
        else:
            value_xerox = value_subdiv.get(f"xer_{name}_{model}")
            if value_xerox is None:
                print(f"В подразделении {self._subdivision.get(from_id_subdiv)}, нет ксерокса {name} {model}")
            else:
                count_ = value_xerox.get("count")
                if count == count_:
                    value = value_subdiv.pop(f"xer_{name}_{model}")
                    value_to_subdiv = self.officeEquipment_lib.get(self._subdivision.get(to_id_subdiv),{})
                    value_to = value_to_subdiv.get(f"xer_{name}_{model}",{})
                    # проверяем, что в подразделении уже есть токое оборудование
                    #if value_to_subdiv is None:
                    self.officeEquipment_lib.setdefault(self._subdivision.get(to_id_subdiv),
                                                            {f"xer_{name}_{model}": value if value_to.get("count",0) == 0
                                                                                          else value.update({"count": count + value_to.get("count")})})
                    #else:
                    #    self.officeEquipment_lib.setdefault(self._subdivision.get(to_id_subdiv), )
                elif count < count_:
                    self.officeEquipment_lib.update({self._subdivision.get(from_id_subdiv):
                                                         value_xerox.update({"count": count_ - count})})

                    self.officeEquipment_lib.update({self._subdivision.get(to_id_subdiv):
                                                        value_xerox.update({"count": count})})
                else:
                    print(f"Ошибка! Вы перемещайте оборудование {name} {model} больше чем есть в подразделении "
                          f"{self._subdivision.get(from_id_subdiv)}")



class OfficeEquipment:
    def __init__(self, name, model):
        self._name = name
        self._model = model

class Printer(OfficeEquipment):
    def __init__(self, name, model, speed_printing, color_printing):
        super().__init__(name, model)
        self._speed_printing = speed_printing
        self._color_printing = color_printing
   # def get_param_printer(self):
    #    return {"name": self.name, "model": self.model, "duplex_scaning": self.du}

class Scanner(OfficeEquipment):
    def __init__(self, name, model, speed_scaning):
        super().__init__(name, model)
        self._speed_scaning = speed_scaning

class Xerox(OfficeEquipment):
    def __init__(self, name, model, duplex_scaning, speed):
        super().__init__(name, model)
        self._duplex_scaning = duplex_scaning
        self._speed = speed

    def get_param_xerox(self, count):
        return {f"xer_{self._name}_{self._model}": {"name": self._name, "model": self._model,
                "duplex_scaning": self._duplex_scaning, "speed": self._speed, "count": count}}
                #    return {"name": self.name, "model": self.model, "duplex_scaning": self.du}

clear = lambda: os.system('cls')

m = Store()
m.add_Xerox(1, "Epson", "cx4300", True, 35, 4)
m.add_Xerox(1, "Epson", "cx4300", True, 35, 2)
m.add_Xerox(2, "Epson", "cx4300", True, 35, 2)
m.add_Xerox(1, "Canon", "lbp1000", True, 15, 10)
m.add_Xerox(3, "Canon", "lbp3000", True, 45, 5)
clear()
m.move_xerox(1, 2, "Epson", "cx4300", 6)

print(m)

#m = Xerox("Epson", "cx4300", True, 35)
#m.test()