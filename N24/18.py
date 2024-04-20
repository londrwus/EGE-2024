f = open('N24\\18.txt').read()

max_v = 0
cnt = 0
l = 0
for i in range(len(f)):
    if f[i] == 'D':
        cnt += 1

    while cnt > 2:
        if f[l] == 'D': 
            cnt -= 1

        l += 1

    if cnt == 2: 
        max_v = max(max_v, i-l+1)

print(max_v)