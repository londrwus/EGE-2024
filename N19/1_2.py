def f(x, h):
    if h == 4 and x >= 34:
        return 1
    elif h == 4 and x < 34:
        return 0
    elif x >= 34 and h < 4:
        return 0
    if h % 2 != 0:
        return any([f(x + 1, h + 1), f(x + 2, h + 1), f(x + 3, h + 1), f(x * 2, h + 1)])
    else:
        return all([f(x + 1, h + 1), f(x + 2, h + 1), f(x + 3, h + 1), f(x * 2, h + 1)])


for x in range(1, 34):
    if f(x, 1) == 1:
        print(x)  # 8 15
