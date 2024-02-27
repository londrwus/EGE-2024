def f(x, stop):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return f(x + 2, stop) + f(x + 4, stop) + f(x + 5, stop)


for i in range(32, 10**3):
    if f(31, i) == 1001:
        print(i)
        break
