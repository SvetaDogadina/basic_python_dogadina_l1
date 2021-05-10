firm = {'Иванов': 170, 'Сидоров': 310, 'Крюков': 190, 'Клюев': 100}
try:
    file_obj = open("sal", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("sal", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"фамилии: {persons}")
print(f"среднее {result}")
