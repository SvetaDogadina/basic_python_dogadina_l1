#  Урок 3 Задание 1 Догадина С
#  Реализовать функцию, принимающую два числа
#  (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя,
#  предусмотреть обработку ситуации деления на ноль
def division(x, y):
    if y != 0:
        print(x / y)
    else:
        print("Делить на ноль нельзя")


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
division(x, y)