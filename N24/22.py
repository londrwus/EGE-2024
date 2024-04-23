f = open('N24\\22.txt').read()

l = 0
cnt = 0
max_v = 9999
for i in range(len(f)):
    if f[i] == '.':
        cnt += 1

    while cnt == 7:
        max_v = min(max_v, i-l+1)
        if f[l] == '.':
            cnt -= 1

        l += 1

print(max_v)