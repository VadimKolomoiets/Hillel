# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

name = input('Введите имя: ')
question = input('Что сделал?: ')
action = input('Куда?: ')
clarification = input('За чем?: ')

with open('example.txt', 'w') as f:
    f.write(name + '\n')
    f.write(question + '\n')

with open('example.txt', 'a') as f:
    f.write(action + '\n')
    f.write(clarification)
