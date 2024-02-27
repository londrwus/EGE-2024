def f(x, stop, step):
    if x > stop:
        return 0
    if step == 15:
        return 1

    return f(x * 2, stop, step + 1) + f(x * 2 + 1, stop, step + 1)


print(f(1, 2**23, 0))  # 32768
