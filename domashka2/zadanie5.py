my_list = [7, 5, 5, 2, 2]
j = 0
while j < 5:
    while True:
        try:
            print("Рейтинг :", my_list)
            answer = int(input("Введите новое знание рейтинга: "))
            break
        except ValueError:
            print("Ошибка! Вы вели не натуральное число")
    i = 0
    while i < len(my_list):
        if answer == my_list[i]:
            my_list.insert(my_list.count(answer) + i, answer)
            break
        elif answer > my_list[i]:
            my_list.insert(i, answer)
            break
        i += 1
    print("Новый рейтинг: ", my_list)
    j += 1
