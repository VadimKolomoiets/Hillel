# Реализовать код, который выведет следующие наборы данных.
# 1) Прибыль по таблице invoice_items. Сумма по заказу = UnitPrice * Quantity (если через sql,
# то нужно использовать sum).
# В итоге через функцию print() выводим 1 цифру общей прибыли.
# 2) Считаем кол-во повторений FirstName в таблице customers. Через функцию print() выводим имя и кол-во его повторений.

import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

query_sql = '''
    SELECT SUM(UnitPrice * Quantity)
      FROM invoice_items
'''

result = cur.execute(query_sql).fetchall()

print(result)


query_sql = '''
    SELECT FirstName
      FROM customers
'''

rows = cur.execute(query_sql).fetchall()

duplicate_first_names = set()
for row in rows:
    duplicate_first_names.add(rows[0])


print(f'all names quantity: {len(rows)}, duplicate names quantity: {len(duplicate_first_names)}')
print(*duplicate_first_names)
