a = set()

def f(x):
    A = x in a
    D = x in range(17, 59)
    C = x in range(29, 81)
    return (D) <= (((not(C)) and (not(A))) <= (not(D)))

for x in range(1, 222):
    if f(x) == 0:
        print(x)
        a.add(x)

print(a)