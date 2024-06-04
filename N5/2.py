sp = []
for x in range(2, 1000):
    n = bin(x)[2:]
    
    if x % 3 == 0:
        n = n + n[-2:]
    else:
        n = n + bin(int((int(x)%3)*3))[2:]
        
    r = int(n, 2)
    if r >= 195:
        sp.append(r)
        
print(min(sp))