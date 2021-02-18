import os


os.system('cls') #очистка экрана

#---------------------------объявление данных----------------------------------
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

#---------------------------программа------------------------------------------

#1-ый блок
key = input('Введите ключ(name или account): ')
key = key.lower()
average_old = (user1['age'] + user2['age'] + user3['age'] + user4['age']) / 4

try:
    print(f"Значение ключа {key} для юзера 1 = {user1[key]}")
    print(f"Значение ключа {key} для юзера 2 = {user2[key]}")
    print(f"Значение ключа {key} для юзера 3 = {user3[key]}")
    print(f"Значение ключа {key} для юзера 4 = {user4[key]}")
    print(f"Средний возраст пользователей: {average_old}")

except KeyError:
    print('Введенный ключ не найден')

#2-ой блок
num_user = input('Введите порядковый номер: ')

if int(num_user) > 0 and int(num_user) <= 4:
    sel_user = user_list[int(num_user) - 1]

    print(f"Данные по юзеру № {num_user}")
    print(f"имя: {sel_user['name']}\nвозраст: {sel_user['age']}")
    print(f"логин: {sel_user['account']['login']}\nпароль: {sel_user['account']['password']}")
else:
    print('Пользователь с указанным номером не найден')

#03-ий блок
num_user = input('Введите номер пользователя, которого нужно переместить в конец списка: ')

if int(num_user) > 0 and int(num_user) <= 4:

    print('Список до изменения:')
    print(user_list)

    sel_user = user_list.pop(int(num_user) - 1)
    move_user = sel_user['name']
    print(f"Пользователь с именем {move_user} перемещен в конец спиcка")
    print(f"Данные пользователя {move_user}:")
    print(sel_user)

    print('Список после изменения:')
    user_list.append(sel_user)
    print(user_list)
else:
    print('Пользователь с указанным номером не найден')
