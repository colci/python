def int_func(str):
    result = ""
    for i in str:
        if (97 <= ord(i) <= 122 or ord(i) == 32):
            result += i
    return result.title()

def MenuInput():
     in_str = input("Введите слова из маленьких латинских букв: ")
     print(int_func(in_str))


MenuInput()