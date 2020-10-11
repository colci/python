i = 1
products = []
while i < 4:
    name_product = ""
    price = 0.0
    count = 0.0
    while True:
        if name_product == "":
            name_product = input("Введите наименование товара: ")
        try:
            if price == 0:
                price = float(input("Введите цену товара: "))
            if count == 0:
                count = float(input("Введите количество товара: "))
        except ValueError:
            print("Ошибка! Вы ввели не число")
            continue
        ed_izm = input("Введите единицу измерения: ")
        break
    products.append((i, {"название": name_product, "цена": price, "количество": count, "ед": ed_izm}))

    i += 1
print(products)
analitic_dic = {}
for product in products:
    for key, value in product[1].items():
        resultValue = analitic_dic.get(key)
        if resultValue is None:
            analitic_dic.update({key: [value]})
        else:
            resultValue.append(value)
print(analitic_dic)

