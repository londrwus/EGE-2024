f = open('N24\\23.txt').read()

cnt = 0
l = 0
min_v = 999999
for i in range(len(f)):
    if f[i] == 'Y':
        cnt = 0
        l = i - 1

    if f[i] == 'X':
        cnt += 1

    while cnt > 500:
        if f[l] == 'X':
            cnt -= 1

        l += 1

    if cnt == 500:
        min_v = min(min_v, i-l+1)

print(min_v)