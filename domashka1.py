# --------------------------------------------  1   -------------------------------------------------------------------
ls = [1,2,True]
print(ls)
print((1,12,1))
print({12,23,12})
num = int(input("Введите число: "))
print("Ваше число", num)

str = input("Как вас зовут? ")
print("Привет", str)

numeric = float(input("Введите число с плавающей точкой: "))
print(numeric)

#--------------------------------------------  2   ---------------------------------------------------------------------

all_second = int(input("Введите количество секунд: "))
all_minuts = all_second // 60
hour = all_minuts // 60
minuts = all_minuts - (hour*60)
second = all_second-(all_minuts * 60)
print(hour, minuts, second)