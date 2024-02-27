def f(x, stop):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return f(x + 1, stop) + f(x + 3, stop) + f(x * 2, stop)


print(f(3, 9) * f(9, 12) * f(12, 20))  # 234
