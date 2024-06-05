f = open('N24\\35.txt').read()

l = 0
fx = 0
fy = 0
mx = 9999999
for x in range(len(f)):
    if f[x] == 'X':
        fx += 1
    
    if f[x] == 'Y':
        fx = 0
        l = x - 1
        
    while fx >= 500:
        mx = min(mx, x - l + 1)
        if f[l] == 'X':
            fx -= 1
            
        l += 1
        
print(mx)