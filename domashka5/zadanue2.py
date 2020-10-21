def readWordsFromFile():
    try:
        moon = open("domashka2.txt", "r", encoding="utf-")
        my_list = moon.readlines()
        moon.close()
        return my_list
    except IOError:
        print("Ошибка при чтении из файла")

my_list = readWordsFromFile()
count_words = len(("".join(my_list)).replace("\n"," ").split(" "))

#count_words = [i.split(" ") for i in my_list]
print(f"В данном файле {len(my_list)} строк и {count_words} слов")
