# Создать словарь в качестве ключа которого будет 6-ти значное число,
# а в качестве значений кортеж состоящий из 2-х элементов – имя(str),
# возраст(int).  Сделать около 5-6 элементов словаря.
# Записать данный словарь на диск в json-файл.

import json

input_data = {
    19990322: ('Tom', 23),
    19970719: ('Alex', 25),
    19851101: ('Nick', 37),
    19700229: ('Sam', 52),
    20010517: ('Sergey', 21),
    19960803: ('David', 26)
}
with open('task_01.json', 'w') as f:
    json.dump(input_data, f)
