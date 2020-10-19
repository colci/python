from sys import argv
def payroll_accounting(hours_worked, cost_hour, bonus):
    print(f"Заработная плата сотрудника: {(hours_worked * cost_hour) + bonus}")

script_name, hours_worked, cost_hour, bonus = argv
if hours_worked.isalnum() and cost_hour.isalnum() and bonus.isalnum():
    payroll_accounting(int(hours_worked), float(cost_hour), float(bonus))
else:
    print("Ошибка! Вы ввели не не числа")
