def f(x, a):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))

for a in range(1, 300):
    if all(f(x, a) == 1 for x in range(3000)):
        print(a)