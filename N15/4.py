def f(x, a):
    return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))

for a in range(1, 3000):
    if all(f(x, a) == 1 for x in range(1, 30000)):
        print(a)