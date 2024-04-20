f = open('N24\\19.txt').read()

max_v = 0
cnt = 0
l = 0
for i in range(len(f)):
    if f[i] == 'T':
        cnt += 1

    while cnt > 100:
        if f[l] == 'T': 
            cnt -= 1

        l += 1

    if cnt == 100: 
        max_v = max(max_v, i-l+1)

print(max_v)