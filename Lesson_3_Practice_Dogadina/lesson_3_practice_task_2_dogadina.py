# Урок 3 Задание 2 Догадина
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод
# данных о пользователе одной строкой

def data_list(**kwargs):
    return list(kwargs.values())


def user_data_list():
    return (data_list(name=input('Enter name: '),
                    s_name=input('Enter second name: '),
                    b_date=input('Enter birth day: '),
                    l_town=input('Enter live town: '),
                    email=input('Enter email: '),
                    tel=input('Enter tel number: ')))


print(' '.join(user_data_list()))