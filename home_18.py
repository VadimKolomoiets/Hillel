# Прочитать сохранённый json-файл из задания №17 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.

import csv
import json

with open('task_01.json', 'r', encoding='utf-8') as f:
    output_data = json.load(f)

print(output_data)

Date_of_Birth = ['19990322', '19970719', '19851101', '19700229', '20010517', '19960803', 'Telephone']
Name = ['Tom', 'Alex', 'Nick', 'Sam', 'Sergey', 'David']
Age = [23, 25, 37, 52, 21, 26]

with open('task_02.csv', 'w', newline='', encoding='utf-8') as f:
    file_writer = csv.writer(f)
    for item in (Date_of_Birth, Name, Age):
        file_writer.writerow(item)

with open('task_02.csv', encoding='utf-8') as f:
    file_reader = csv.reader(f)
    for item in file_reader:
        print(item)
