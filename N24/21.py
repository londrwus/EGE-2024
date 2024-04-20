f = open('N24\\21.txt').read()

cnt = 0
l = 0
m = 0
for i in range(1, len(f)):
    if i > 2 and (f[i-2] + f[i-1] + f[i] == 'ORO' or f[i-2] + f[i-1] + f[i] == 'ROR'):
        cnt = 0
        l = i - 1

    if f[i-1] + f[i] == 'RO':
        cnt += 1

    while cnt > 21:
        if f[l] + f[l+1] == 'RO':
            cnt -= 1

        l += 1

    if cnt == 21:
        m = max(m, i - l + 1)

print(m)