a = set(i for i in range(1000))
p = {i for i in range(2, 21, 2)}
q = {i for i in range(3, 31, 3)}

def f(x):
    P = x in p
    Q = x in q
    A = x in a
    
    return ((A) <= (P)) and (not(Q) <= (not(A)))
    
for x in range(1000):
    if f(x) == 0:
        a.remove(x)
        
print(len(a))