# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

value = 1
result = 0
num = int(input("Введите число: "))

for item in range(value, num+1):
    if item % 3 != 0:
        result += item ** 3

print(f'Res: {result}')

result = 0
while num > 0:
    if num % 3 != 0:
        result += num ** 3
    num -= 1

print(f'Res: {result}')
