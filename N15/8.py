a = set()
c = {1, 3, 5, 7, 9, 11}
b = {3, 6, 9, 12}

def f(x):
    C = x in c
    B = x in b
    A = x in a
    return ((C) <= (not(B))) or (A)

for x in range(1000):
    if f(x) == 0:
        a.add(x)

print(a)