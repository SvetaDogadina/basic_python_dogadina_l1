# Урок 2 Задание 3 Догадина.
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict
# Решение dict
seasons = dict(
    {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
     11: 'осень', 12: 'зима'})
month = int(input("Введите номер месяца по порядку: "))
try:
    print("Этот месяц относится к сезону", seasons[month])
except KeyError:
    print("Месяца с таким номером нет")
# Решение list
season_list = [False, 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень',
               'осень', 'зима']
x = int(input("Введите номер месяца по порядку: "))
if x == 0:
    print("Негодник, нулевого месяца не бывает! Иди учи натуральные числа")
else:
    try:
        print("Этот месяц принадлежит сезону", season_list[x])
    except IndexError:
        print("Месяца с таким номером нет")
