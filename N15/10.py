from itertools import *

def f(x):
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not(A))) <= (not(P)))

b = [i/4 for i in range(16*4, 84*4+1)]
m = []

for a1, a2 in combinations(b, 2):
    if all(f(x) == 1 for x in b):
        m.append(a2 - a1)

print(min(m))