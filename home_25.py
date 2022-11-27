# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.

import math


class Calculator:
    a = 21
    b = 7
    res1 = a + b
    try:
        def __add__(self):
            return res1

    except NameError as error:
        print('NameError:', error)
    except ZeroDivisionError as error:
        print('ZeroDivisionError:', error)

    try:
        res2 = a - b

        def __sub__(self, other):
            return res2

    except NameError as error:
        print('NameError:', error)
    except ZeroDivisionError as error:
        print('ZeroDivisionError:', error)

    try:
        res3 = a * b

        def __mul__(self, other):
            return res3

    except NameError as error:
        print('NameError:', error)
    except ZeroDivisionError as error:
        print('ZeroDivisionError:', error)

    try:
        res4 = a / b

        def __truediv__(self, other):
            return res3

    except ZeroDivisionError as error:
        print('ZeroDivisionError:', error)
    except Exception as error:
        print('Exception:', error)

    try:
        res5 = a ** 2
        res_5 = b ** 3

        def __pow__(self, power, modulo=None):
            return res5, res_5

    except ZeroDivisionError as error:
        print('ZeroDivisionError:', error)
    except Exception as error:
        print('Exception:'), error

    print(math.sqrt(a ** 1 / 2))
    print(math.sqrt(b ** 1 / 2))


calculator = Calculator
print(calculator.res1)
print(calculator.res2)
print(calculator.res3)
print(calculator.res4)
print(calculator.res5)
print(calculator.res_5)
