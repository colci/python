def writeInFile(inputData):
    try:
        moon = open("inputData.txt", "a", encoding="utf-")
        moon.write(inputData + "\n")
        moon.close()
    except IOError:
        print("Ошибка при записи в файл")

print("Ведите данные для записи в файл: ")
while True:
    inputData = input()
    if inputData == "":
        break
    writeInFile(inputData)
