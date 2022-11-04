# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’
# И на конец результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).

text_bytes = b'r\xc3\xa9sum\xc3\xa9'

text_str = text_bytes.decode()
print(text_str)

text_bytes_2 = text_str.encode('Latin1')
print(text_bytes_2)

text_str_2 = text_bytes_2.decode('Latin1')
print(text_str_2)
