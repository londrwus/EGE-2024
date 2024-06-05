from itertools import combinations

def f(x):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return (C) <= (((not(A)) and (B)) <= (not(C)))
    
b = [i/4 for i in range(23*4, 116*4+1)]
m = []
    
for a1, a2 in combinations(b, 2):
    if all(f(x) == 1 for x in b):
        m.append(a2 - a1)
        
print(min(m))