sp = []
for x in range(2, 5000):
    n = bin(x)[2:]
    
    if x % 2 == 0:
        n = '10' + str(n)
    else:
        n = '1' + str(n) + '01'
        
    r = int(n, 2)
    if r >= 516:
        sp.append(x)
        
print(min(sp))