a = set([i for i in range(1000)])
c = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
b = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

def f(x):
    C = x in c
    B = x in b
    A = x in a
    return ((A) <= (C)) and ((B) <= (not(A)))

for x in range(1000):
    if f(x) == 0:
        a.remove(x)

print(len(a))