# Урок 1 Практика Догадина Светлана
# Задание 2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс
# Используйте форматирование строк.
seconds = int(input("Enter the time in seconds: "))
minutes = seconds // 60
hours = minutes // 60
print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))