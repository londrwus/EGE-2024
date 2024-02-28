def f(x, h):
    if (h == 3 or h == 5) and x >= 34:
        return 1
    elif h == 5 and x < 34:
        return 0
    elif x >= 34 and h < 5:
        return 0

    if h % 2 == 0:
        return any([f(x + 1, h + 1), f(x + 2, h + 1), f(x + 3, h + 1), f(x * 2, h + 1)])
    else:
        return all([f(x + 1, h + 1), f(x + 2, h + 1), f(x + 3, h + 1), f(x * 2, h + 1)])


for x in range(1, 34):
    if f(x, 1) == 1:
        print(x)
