def fact(n):
    for j in [i + 1 for i in range(n)]:
        yield j


for el in fact(5):
    print(el)