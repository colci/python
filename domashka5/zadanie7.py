import json

def parsing_file():
    try:
        my_list = []
        list_profit = []
        result = {}
        with open("text7.txt", "r", encoding="utf-") as lib:
            for el in lib.readlines():
                my_list.append(el.replace("\n","").split(" "))
                list_profit = [[el[0], float(el[2])-float(el[3]), float(el[2])-float(el[3]) if(float(el[2])-float(el[3]) > 0) else 0,
                                    1 if (float(el[2])-float(el[3]) > 0) else 0] for el in my_list]
            for el in list_profit:
                result.update({el[0]: el[1]})
        return [result, {"average_profit": float((sum([i[2] for i in list_profit]))/(sum([i[3] for i in list_profit])))}]
    except IOError:
        print("Ошибка при работе с файлом")

def add_in_json(text_json):
    try:
        with open("text7_json.txt", "w", encoding="utf-") as setjson:
            json.dump(text_json, setjson)
    except IOError:
        print("Ошибка при записи в файл")


ls_json = parsing_file()
add_in_json(ls_json)