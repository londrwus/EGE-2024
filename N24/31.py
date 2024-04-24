f = open('N24\\31.txt').read().strip()

m = 0
l = 0
fx = 0
for i in range(len(f)):
    if f[i] == 'F': fx += 1

    while fx > 1:
        if f[l] == 'F': fx -= 1
        l += 1

    if fx == 1:
        m = max(m, i - l + 1)

print(m)