f = open('N24\\20.txt').read()

max_v = 0
l = 0
cnt = 0
for i in range(len(f)):
    if f[i-1] + f[i] == 'AB':
        cnt += 1

    while cnt > 50:
        if f[l] + f[l+1] == 'AB':
            cnt -= 1

        l += 1

    if cnt == 50:
        max_v = max(max_v, i-l+1)

print(max_v)