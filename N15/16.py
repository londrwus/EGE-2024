from itertools import combinations

def f(x):
    A = a1 <= x <= a2
    P = 16 <= x <= 84
    Q = 27 <= x <= 43
    
    return (((A) <= (P)) or (Q))

b = [i / 4 for i in range(16*4, 84*4+1)]
m = []

for a1, a2 in combinations(b, 2):
    if all(f(x) for x in b):
        m.append(a2 - a1)
        
print(max(m))