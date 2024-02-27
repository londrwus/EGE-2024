def calc(x):  # this is shitcode just better do x % 10 != 9 idk why i did it
    if str(x)[0] == "9" and str(x)[1] == "9":
        return int(x)
    if str(x)[0] == "9":
        return int(x) + 1
    if str(x)[1] == "9":
        return int(x) + 10

    return int(x) + 11


def f(x, stop):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return f(x + 1, stop) + f(calc(x), stop)


print(f(25, 51))  # 116
