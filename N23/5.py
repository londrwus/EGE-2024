def f(x, stop):
    if x > stop or x == 43:
        return 0
    if x == stop:
        return 1

    return f(x + 2, stop) + f(x + (x - 1), stop) + f(x + (x + 1), stop)


print(f(7, 63))  # 116
