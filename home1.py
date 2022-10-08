# 1. Создать 3 переменные с одинаковыми данными (и по значению и по типу) и с одинаковыми идентификаторами
# 2. Создать 2 переменные с одинаковыми данными (и по значению и по типу) и с разными идентификаторами
# 3. *Поменять их типы так, чтобы у 1-х трёх были разные идентификаторы,
#    а у 2-х последних были одинаковые идентификаторы. При этом присваивать переменным другие значения или
#    присваивать их друг другу нельзя. Все три переменные необходимо приводить к одному и тому же типу,
#    точно так же и обе последние переменные необходимо приводить к одному и тому же типу.

a = 7
b = 7
c = 7

print(a == b), print(type(a))
print(a == c), print(type(b))
print(b == c), print(type(c))
print(a is b), print(id(a))
print(a is c), print(id(b))
print(b is c), print(id(c))

a_1 = [13]
b_1 = [13]

print(a_1 == b_1), print(type(a_1)), print(type(b_1))
print(a_1 is b_1), print(id(a_1)), print(id(b_1))

a = [7]
b = [7]
c = [7]


print(a == c), print(type(a))
print(a == b), print(type(b))
print(b == c), print(type(c))
print(a is b), print(id(a))
print(a is c), print(id(b))
print(b is c), print(id(c))

a_1 = 13
b_1 = 13

print(a_1 == b_1), print(type(a_1)), print(type(b_1))
print(a_1 is b_1), print(id(a_1)), print(id(b_1))
