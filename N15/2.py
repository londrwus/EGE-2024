def f(x, a):
    return ((x % a == 0) and (x % 24 == 0) and (not(x % 16 == 0))) <= (not(x % a == 0))

sp = []
for a in range(1, 300):
    if all(f(x, a) == 1 for x in range(1, 3000)):
        sp.append(a)

print(min(sp))