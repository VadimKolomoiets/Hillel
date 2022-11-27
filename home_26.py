# Создать генератор геометрической прогрессии

def geomprog(n, sl, res=1):
    if sl == 0:
        print(res)
    else:
        res *= n
        geomprog(n, sl - 1, res)


geomprog(5, 7)
