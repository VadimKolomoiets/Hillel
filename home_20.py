# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    brand = 'BMW_AG'
    age = 2003
    color = True
    mark = 'BMW'
    weight = True


    def __init__(self, brand='BMW_AG', mark='BMW', age=2003):
        self.brand = brand
        self.mark = mark
        self.age = age


    def move(self):
        print('<<move>>')


    def birthday(self):
        print(self.age + 1)



    def stop(self):
        print('<<stop>>')



auto = Auto()
auto.move()
auto.stop()
auto.birthday()
