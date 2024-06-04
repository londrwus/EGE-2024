sp = []
for x in range(1, 500):
    n = bin(int(x))[2:]
    
    if x % 2 == 0:
        n = str(n) + '00'
    else:
        n = str(n) + '11'
        
    r = int(n, 2)
    if r < 134:
        sp.append(x)
        
print(max(sp))