from functools import reduce

def get_list_even_number():
    return [el for el in range(100, 1001) if el % 2 == 0]

def product_number(val1, val2):
    return val1 * val2

print(reduce(product_number, get_list_even_number()))
