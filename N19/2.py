def f(x, h):
    if h == 3 and x >= 36:
        return 1
    elif h == 3 and x < 36:
        return 0
    elif x >= 36 and h < 3:
        return 0

    if h % 2 != 0:
        return any([f(x + 1, h + 1), f(x * 2, h + 1), f(x * 3, h + 1)])
    else:
        return all([f(x + 1, h + 1), f(x * 2, h + 1), f(x * 3, h + 1)])


for x in range(1, 36):
    if f(x, 1) == 1:
        print(x)  # 16
