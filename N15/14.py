def f(x, y, a):
    return ((a < x) or (x**2 - 7 * x + 10 > 0)) and ((a >= y) or (y**2 + 7 * y + 12 > 0))

for a in range(-300, 300):
    if all(f(x, y, a) == 1 for x in range(-300, 300) for y in range(-300, 300)):
        print(a)