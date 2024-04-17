def f(x, y, a):
    return ((x * y) > a) and (x > y) and (x < 8)

for a in range(1, 300):
    if all(f(x, y, a) == 0 for x in range(3000) for y in range(3000)):
        print(a)