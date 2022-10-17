# Сделать программу в виде функций в которой нужно будет угадывать число.

import random
random_value = random.randint(0, 100)
attempt = 0
print("Компьютер загадал число от 0 до 100 и у вас 10 попыток, чтобы отгадать число")

for i in range(1, 11):
    choice = int(input("Введите число: "))
    if choice > random_value:
        print('много')
    elif choice < random_value:
        print('мало')
    else:
        print(f"Вы угадали число с {i}-ой попытки")
        break
    attempt += 1
    print(f"Вам осталось {10 - attempt} попыток")

if attempt >= 10:
    print(f"Вы исчерпали 10 попыток. Было загадано {random_value}")

