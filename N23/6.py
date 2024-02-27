def f(x, stop):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return (
        f(x + 1, stop)
        + f(int(str(bin(x)[2:]) + "0", 2), stop)
        + f(int(str(bin(x)[2:]) + "1", 2), stop)
    )


print(f(4, 29))  # 79
