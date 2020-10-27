def parsing_file():
    try:
        result = {}
        with open("text6.txt", "r", encoding="utf-8") as lib:
            for el in lib.readlines():
                #result = el.split(" ")
                isum = 0
                key = ""
               # for i in result:
                for i in el.split(" "):
                    end = i.find("(")
                    sep = i.find(":")
                    if(end > -1):
                        isum = isum + float(i[0:end])
                    if(sep > -1):
                      key = i[0:sep]
                result.update({key: isum})
        return result
    except IOError:
        print("Ошибка при работе с файлом")

print(parsing_file())