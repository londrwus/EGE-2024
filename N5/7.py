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
    
    if x % 2 == 0:
        n = '2' + n + conv(int(n[-1]) * 2, 3)
    else:
        n = conv(int(n[0]) * 2, 3) + n + '2'
        
    r = int(n, 3)
    if r > 100:
        sp.append(r)
        
print(min(sp))