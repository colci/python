def getSalaryEmployees():
    try:
        moon = open("employees.txt", "r", encoding="utf-")
        infoSalary = moon.readlines()
        moon.close()
        return infoSalary
    except IOError:
        print("Ошибка при записи в файл")


infoSalary = getSalaryEmployees()
new_list = [[i[0], float(i[1])] for i in [el.replace("\n","").split(" ") for el in infoSalary]]
print("Список сотрудников у которых зарплата ниже 20000:")
for name in [el[0] for el in new_list if el[1] < 20000]:
    print(name)

print("Средняя велечина дохода струдников = {0:0.2f}".format(sum([i[1] for i in new_list])/len(infoSalary)))
