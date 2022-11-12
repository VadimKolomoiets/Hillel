# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_load.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.

import time


class Auto:
    brand = 'BMW_AG'
    age = 2003
    mark = 'BMW'

    def __init__(self, brand='BMW_AG', mark='BMW', age=2003):
        self.brand = brand
        self.mark = mark
        self.age = age

    def move(self):
        print('<<move>>')


    def load(self):
        time.sleep(1)
        print('<<load>>')
        time.sleep(1)


class Truck(Auto):
    max_load = '2000-kg'
    wheels = 10


    def move(self):
        super().move()
        print('<<attention>>')


class Car(Auto):
    max_speed = '280-km/h'
    wheels = 4

    def move(self):
        super().move()
        print('<<max_speed is 2000-kg')


truck = Truck()
truck.move()

auto = Auto()
auto.move()
auto.load()

car = Car()
car.move()

