def f(x, stop):
    if x < stop:
        return 0
    if x == stop:
        return 1

    return f(x - 2, stop) + f(x - 5, stop)


print(f(23, 2))  # 29
