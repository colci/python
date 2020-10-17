def MenuInput():
    res = 0
    final_amount = 0
    exit_ = False
    print("Введите строки чисел, разделенных пробелом для расчета их суммы.","\n",
          "Для выхода нажмите q", sep="")
    while True:
        res = 0
        input_list = input().split()
        for i in input_list:
            res = sumVal(res, i)
            findIndex = (i.upper()).find("Q")
            if (findIndex > -1):
                res = sumVal(res, i[0:findIndex])
                exit_ = True
                break
        final_amount += res
        print(f"{res}({final_amount})")
        if exit_ == True:
            break

def sumVal(Val1, val2):
   # resVal = 0
    #if type(val2) == int or type(val2) == float:
    if check_float(val2):
        Val1 += float(val2)
    return Val1

def check_float(str):
    try:
        num = float(str)
        return True
    except ValueError:
        return False

MenuInput()
