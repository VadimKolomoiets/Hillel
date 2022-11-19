# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18

    @staticmethod
    def is_young(age):
        return age < 18


person1 = Person('Sarah', 21)
person2 = Person.from_birth_year('Roark', 1996)

print(Person.class_method())
print(person1.age)
print(person2.age)

print(Person.is_adult(22))
print(Person.is_young(15))

