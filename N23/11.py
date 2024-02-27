sp = set()


def f(x, step):
    if step == 8:
        sp.add(x)
        return 1

    return f(x + 1, step + 1) + f(x + 5, step + 1) + f(x * 3, step + 1)


f(1, 0)
print(sorted(sp, reverse=True))  # ans is 1 cuz 1017 is the only one in range 1000, 1024
