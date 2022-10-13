# Используя input() ввести предложение состоящее из двух слов.
# Создать 2 переменные и в каждую записать по 1 введённому слову используя методы строк.
# Создать новую переменную 3-мя разными способами форматирования (фактически 3 переменные),
# которая бы состояла из введённых слов в обратном порядке, первое слово должно состоять
# только из больших букв, а второе с первой заглавной буквы и остальных маленьких.
# В начале предложения должен быть восклицательный знак, а в конце вопросительный.
# Используя только атрибуты функции print() вывести первоначальную строку и получившиеся
# разными способами форматирования через разделитель "<<<>>>", вывод сделать в файл.

club = input("Name team: ")
name = (club[:4]).upper()           # Name Team = Реал Мадрид
city_name = (club[5:]).lower()

name_1 = 'Вадим'
age = 23

v_1 = ("Меня зовут %s, мне %d года, %s любит играть в футбол" %(name_1.upper(), age, name_1))

v_2 = ("Меня зовут {}, мне {} года, {} любит играть в футбол".format(name_1
                                                                .upper(), age, name_1))

v_3 = (f"Меня зовут {name_1.upper()}, мне {age} года, {name_1}"
      f" любит играть в футбол")

v_1 += "!"
v_2 += "!"
v_3 += "!"

s_file = open('home__3.txt', 'w')

print(name, file=s_file)
print(city_name, file=s_file)


print(sep="<<<>>>", file=s_file)

print(v_1[::-1], end="?\n", file=s_file)
print(v_2[::-1], end="?\n", file=s_file)
print(v_3[::-1], end="?", file=s_file)

s_file.close()