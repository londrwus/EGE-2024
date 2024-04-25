def f(x, stop):
    if x < stop:
        return 0
    if x == stop:
        return 1
    
    return f(x - 8, stop) + f(x // 2, stop)

print(f(102, 43) * f(43, 5))