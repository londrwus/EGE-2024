sp = []
for x in range(2, 50000):
    n = bin(x)[2:]
    
    n = n + n[-1]
    n = n + str(sum(int(c) for c in n) % 2)
    
    r = int(n, 2)
    if r < 13500:
        sp.append(r)
        
print(max(sp))