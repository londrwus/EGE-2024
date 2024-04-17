f = open('N24\\14.txt').read().strip()
m = [''] * len(f)

cnt = 0
for i in range(1, len(f)):
    if f[i] < f[i-1]:
        if len(m[cnt]) == 0:
            m[cnt] = f[i-1]

        m[cnt] += f[i]
    else:
        cnt += 1

print(m)