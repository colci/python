ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for i, el in enumerate(ls) if el > (ls[i-1] if i > 0 else ls[i])]
print(result_list)
