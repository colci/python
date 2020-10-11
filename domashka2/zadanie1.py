ls = [1,2,True,"str",{1,2},4.5,[1,5]]
for i in ls:
    if (type(i) is int):
        print(f"Значение {i} типа int")
    elif(type(i) is str):
        print(f"Значение {i} типа str")
    elif(type(i) is float):
        print(f"Значение {i} типа float")
    elif(type(i) is list):
        print(f"Значение {i} типа list")
    elif(type(i) is bool):
        print(f"Значение {i} типа bool")
    elif(type(i) is set):
        print(f"Значение {i} типа set")