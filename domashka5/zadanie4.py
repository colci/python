from googletrans import Translator
translator = Translator()

def get_list_data ():
    try:
        result = []
        with open("text4.txt", "r", encoding="utf-") as lib_translate:
            for el in lib_translate.readlines():
                result.append(el.split("-"))
            return result
    except IOError:
        print("Ошибка при записи в файл")

def add_in_file(line):
    try:
        with open("new_text4.txt", "a", encoding="utf-") as setlib:
            setlib.write(line)
    except IOError:
        print("Ошибка при записи в файл")

ls = get_list_data()
for line in ls:
    translate = translator.translate(line[0], "ru", "en")
    add_in_file(f"{translate.text}-{line[1]}")


