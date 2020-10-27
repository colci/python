from datetime import datetime

class TrafficLight:
    __color = "Красный"

    def running(self):
        list_colors = ["Красный", "Желтый", "Зеленый", "Желтый"]
        lib = {"Красный": 7, "Желтый": 2, "Зеленый": 4}
        start_date = datetime.now()
        i = 0
        print(self.__color)
        while True:
            current_date = datetime.now()
            if (current_date - start_date).total_seconds() >= lib.get(list_colors[i]):
                if (i == 3):
                    #i = 0 - c этой строчкой будет рабо как настоящий светафор
                    break # это закоментировать))
                else:
                    i += 1
                start_date = datetime.now()
                __color = list_colors[i]
                print(list_colors[i])


a = TrafficLight()
a.running()
