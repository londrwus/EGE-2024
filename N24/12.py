f = open('N24\\12.txt').read()

cnt = 1
max_v = 0
for i in range(1, len(f)):
    if f[i] >= f[i-1]:
        cnt += 1
        max_v = max(max_v, cnt)
    else:
        cnt = 1

print(max_v)