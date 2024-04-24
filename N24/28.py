f = open('N24\\28.txt').read()

kx = 0
ky = 0
l = 0
m = 0
for i in range(len(f)):
    if f[i] == 'X':
        kx += 1
    if f[i] == 'Y':
        ky += 1

    while kx > 1 or ky > 1:
        if f[l] == 'X': kx -= 1
        if f[l] == 'Y': ky -= 1

        l += 1

    if kx == 1 and ky == 1:
        m = max(m, i - l + 1)

print(m)