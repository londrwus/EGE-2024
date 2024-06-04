sp = []
for x in range(100, 1000):
    n = str(x)
    l1 = int(n[0]) * int(n[1])
    l2 = int(n[1]) * int(n[2])
    n = str(l2) + str(l1)
    if n == '205':
        sp.append(x)
        
print(min(sp))