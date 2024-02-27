def f(x, stop, step):
    if x > stop:
        return 0
    if x == stop and step == 7:
        return 1

    return (
        f(x + 1, stop, step + 1) + f(x + 4, stop, step + 1) + f(x * 2, stop, step + 1)
    )


print(f(3, 27, 0))  # 37
