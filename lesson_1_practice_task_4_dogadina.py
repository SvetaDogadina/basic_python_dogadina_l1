# Урок 1 Практика Догадина Светлана
# Задание 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
x = int(input("Enter any positive integer:"))
y = x%10
x = x//10
#print(y)
#print(x)
while x > 0:
    if x % 10>y:
        y = x%10
    x = x//10
    #print(x, x % 10)
print("The biggest number in your integer is ",y)
