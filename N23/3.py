def f(x, stop):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return f(x + 1, stop) + f(x * 2, stop)


print(f(1, 10) * f(10, 20))  # 28
