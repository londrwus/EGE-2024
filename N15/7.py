def f(x, y, a):
    return (x > 39) or (y > 26) or ((2 * x + 4 * y) < a)

for a in range(1, 300):
    if all(f(x, y, a) == 1 for x in range(3000) for y in range(3000)):
        print(a)