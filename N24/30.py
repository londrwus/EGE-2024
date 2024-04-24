f = open('N24\\30.txt').read().strip()

cnt = 3
m = 0
for i in range(len(f) - 3):
    if f[i] + f[i+1] + f[i+2] + f[i+3] != 'AXMM':
        cnt += 1
        m = max(m, cnt)
    else:
        cnt = 3

print(m)