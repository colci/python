ls = list(input("Введите список значений: ").replace(" ", ""))
print(ls)
i = 0
count = len(ls)
while i in range(0, count if count % 2 == 0 else count - 1, 2):
    ls[i], ls[i+1] = ls[i+1], ls[i]
    i += 2
print(ls)
