def f(x, stop, step):
    if x > stop:
        return 0
    if x == stop:
        return 1

    if step == "*":
        return f(x + 1, stop, step="+") + f(x + 2, stop, step="+")
    else:
        return (
            f(x + 1, stop, step="+")
            + f(x + 2, stop, step="+")
            + f(x * 2, stop, step="*")
        )


print(f(1, 15, ""))  # 1545
