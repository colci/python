def get_sum_nubers():
    try:
        my_list = [1,3,4,5,6,7,8,89,42,56]
        with open("text5.txt", "w+", encoding="utf-") as lib_translate:
            for el in my_list:
                lib_translate.write(f"{el}")
            lib_translate.seek(0)
            return sum(map(float,lib_translate.read().split()))
    except IOError:
        print("Ошибка при записи в файл")

print(get_sum_nubers())