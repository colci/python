class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"{self.color} автомобиль {self.name} поехал")
        self.show_speed()

    def stop(self):
        print(f"{self.color} автомобиль {self.name} остановился")
        self.speed = 0

    def turn(self, direction):
        print(f"{self.color} автомобиль {self.name} поехал {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} состовляет {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if (self.speed > 60):
            print(f"Городской автомобиль {self.name} движется со скоростью {self.speed} и превысил скорость на {self.speed - 60} км/ч")
        else:
            print(
                f"Городской автомобиль {self.name} движется со скоростью {self.speed} и превысил скорость на {self.speed - 60} км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Грузовой автомобиль превысил скорость на {self.speed -40} км/ч")

class PoliceCar(Car):
    pass

list_direction = ["на лево", "на право", "прямо", "в обратном направлении"]
auto_police = PoliceCar("Черный", "FORD", True)
auto_police.go(100)
auto_police.turn(list_direction[0])
auto_police.turn(list_direction[3])
auto_police.stop()

auto_work = WorkCar("Желтый", "KAMAZ", False)
auto_work.go(50)
auto_work.turn(list_direction[2])
auto_work.speed = 45
auto_work.show_speed()
auto_work.turn(list_direction[3])

sport_auto = SportCar("Красный", "Porsh", False)
sport_auto.go(120)
sport_auto.turn(list_direction[2])
sport_auto.turn(list_direction[1])
sport_auto.turn(list_direction[0])
sport_auto.stop()

town_auto = TownCar("Синий", "Lada", False)
town_auto.go(80)
town_auto.turn(list_direction[2])
town_auto.turn(list_direction[1])
town_auto.speed = 100
town_auto.show_speed()
town_auto.turn(list_direction[0])
town_auto.stop()
