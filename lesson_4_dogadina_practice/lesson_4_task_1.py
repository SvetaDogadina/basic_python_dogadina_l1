# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами
from sys import argv
address, salary_per_hour, hours, bonus = argv
print("Путь: ", address)
print("Ставка в час: ", salary_per_hour)
print("Часы: ", hours)
print("Премия: ", bonus)
salary_per_hour = int(salary_per_hour)
hours = int(hours)
bonus = int(bonus)
salary = ((salary_per_hour * hours) + bonus)
print("Расчет заработной платы: ", salary)
