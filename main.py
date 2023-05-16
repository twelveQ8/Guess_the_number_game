
# шаг 1 загадать случайное число +
import random
numbers = random.randint(1, 100)

# пользователь должен угадать число 2
user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input("Выберите уровень сложности от 1 до 3: "))

max_count = levels[level]
user_count = int(input('Введите количество пользователей: '))
users = []

is_winner = False
winner_name = None

for i in range(user_count):
    user_name = input(f'Введите имя пользователя. {i + 1}: ')
    users.append(user_name)
print(f'Игроки, которые участвуют в игре - {users}')


while not is_winner:
    count += 1

    if count > max_count:
        print(f"Все пользователи проиграли... {numbers}")
        break
        
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input("Введите число: "))
        if user_number == numbers:
            is_winner = True
            winner_name = user
            break
        elif numbers < user_number:
            print('Число больше загаданного. ')
        else:
            print("Ваше число меньше загаданного. ")
# сравнить введеное число с загаданным
else:
    print(f"Победитель {winner_name}")
# цикл
