def sumMax(val_1, val_2, val_3):
    ls = f"{val_1}  {val_2}  {val_3}".split()
    ls = list(map(int, ls))
    ls.sort()
    ls.pop(0)
    return sum(ls)


sumMax(4566, 4, 7)