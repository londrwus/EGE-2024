def conv(num, radix):
    digits = '012'
    final = ''
    while num > 0:
        k = num % radix
        final = digits[k] + final
        num = num // radix
        
    return final

sp = []
for x in range(2, 5000):
    n = conv(x, 3)
    
    if x % 7 == 0:
        n = n + str(n)[-2:]
    else:
        n = n + conv((x % 7) * 3, 3)
        
    r = int(n, 3)
    if r > 369:
        sp.append(r)
        
print(min(sp))