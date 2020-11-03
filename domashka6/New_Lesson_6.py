#  -------------------------------------------------------- 1 ----------------------------------------------------------

import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficlight_1 = TrafficLight()
trafficlight_1.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep


class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------



import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def __init__(self, light_list):
        self.light_list = light_list

    def running(self):
        if len([i for i in self.light_list if i in ["red", "yellow", "green"]]) >= 3:
            for light in itertools.cycle(self.__color):
                print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
                time.sleep(light[1][0])
        else:
            print("Your color list is incorrect.")


trafficlight_1 = TrafficLight(["lilac", "green", "lime", "white", "black", "yellow"])
trafficlight_1.running()


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep


class TrafficLight:
    __color = 0

    def running(self):
        # [красный, жёлтый, зелёный]
        lights = [
            {
                'name': 'красный',
                'color': '\x1b[41m',
                'delay': 7
            },
            {
                'name': 'жёлтый',
                'color': '\x1b[43m',
                'delay': 2
            },
            {
                'name': 'зелёный',
                'color': '\x1b[42m',
                'delay': 5
            }
        ]

        print('\nИмитация работы светофора:\n')

        while True:
            # формируем строку вывода (светофор)
            s = ''
            for i in range(3):
                if i == self.__color:
                    s += f'({lights[self.__color]["color"]}   \x1b[0m)'
                else:
                    s += '(   )'

            print(f'\r{s}', end='')
            # устанавливаем задержку
            sleep(lights[self.__color]["delay"])
            # меняем цвет
            self.__color = (self.__color + 1) % 3


lights = TrafficLight()
lights.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import pygame


class TrafficLight:
    WHITE = (255, 255, 255)
    GRAY = (125, 125, 125)
    GREEN = (0, 255, 64)
    YELLOW = (225, 225, 0)
    RED = (255, 0, 0)

    clr = [RED, YELLOW, GREEN, YELLOW]

    def __init__(self):
        self.act_time = [2, 7, 2, 7]

    def switch_on(self):
        FPS = 60
        WIN_WIDTH = 120
        WIN_HEIGHT = 400

        pygame.init()
        clock = pygame.time.Clock()

        sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # радиус и координаты круга
        r = WIN_WIDTH // 4
        x = WIN_WIDTH // 2
        y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали

        k = 0

        while 1:
            sc.fill(self.GRAY)
            pygame.draw.circle(sc, self.WHITE, (x, y - 100), r)
            pygame.draw.circle(sc, self.WHITE, (x, y), r)
            pygame.draw.circle(sc, self.WHITE, (x, y + 100), r)

            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()

            if k == 0:
                pygame.draw.circle(sc, self.clr[k], (x, y - 100), r)
            elif k == 1 or k == 3:
                pygame.draw.circle(sc, self.clr[k], (x, y), r)
            elif k == 2:
                pygame.draw.circle(sc, self.clr[k], (x, y + 100), r)

            pygame.display.update()
            pygame.time.wait(self.act_time[k] * 1000)

            if k >= 3:
                k = 0
            else:
                k += 1

            clock.tick(FPS)


###########

a = TrafficLight()
a.switch_on()


#  -------------------------------------------------------- 2 ----------------------------------------------------------


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def calc(self):
        print(f"Масса асфальта - {self._lenght * self._width * 25 * 5 / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Enter width of road in m: ")), int(input("Enter lenght of road in m: ")))
            road_1.calc()
            break
        except ValueError:
            print("Only integer!")


#  -------------------------------------------------------- 3 ----------------------------------------------------------


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


meneger = Position("Dorian", "Grey", "СEO", 500000, 125000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())


#  -------------------------------------------------------- 4 ----------------------------------------------------------

class Car:
    ''' Автомобиль '''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):
    ''' Городской автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    ''' Грузовой автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    ''' Спортивный автомобиль '''


class PoliceCar(Car):
    ''' Полицейский автомобиль '''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Полицайка"', 'белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Грузовичок"', 'хаки', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('"Спортивка"', 'красный', 120)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Малютка"', 'жёлтый', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')

#  -------------------------------------------------------- 5 ----------------------------------------------------------


class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}))")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")


stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
marker = Marker("COPIC")
marker.draw()

