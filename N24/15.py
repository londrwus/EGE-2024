f = open('N24\\15.txt').read()

cnt = 0
max_v = 0
for i in range(0, len(f) - 1, 2):
    if f[i] + f[i+1] == 'BB' or f[i] + f[i+1] == 'DD':
        cnt += 1
        max_v = max(max_v, cnt)
    else:
        cnt = 0

print(max_v)