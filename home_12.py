# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()


from datetime import datetime


def time_dec(a_func):
    def wishper(*args, **kwargs):
        time = datetime.now()
        result = a_func(*args, **kwargs)
        all_time = datetime.now() - time
        print('Время выполнения функции: ', all_time.microseconds, 'микросекунд')
        return result
    return wishper


@time_dec
def sum_list():
    print('sum_list')
    return sum([number for number in range(100000)])


print(sum_list())


@time_dec
def func(number):
    print('func')
    res = 1
    for num in range(1, number + 1):
        res *= num
    return res


print(func(10000))
