# Урок 1 Практика Догадина Светлана
# Задание 1
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран
# Ответ: создадим- шутку "Dumb 64bit"
name = input("Enter your name: ")
print("Hi, " + name)
year_of_birth = int(input("Enter your year of birth in YYYY format: "))
age = str(2021 - year_of_birth)
print("So you are " + age + " years old?")
answer = input("Type answer YES or NO: ")
if answer == "YES":
    print("Cool! My 64bit works good today")
if answer == "NO":
    print("You are drunk! Go home")
