f = open('N24\\26.txt').read()

cnt = 0
m = 0
idx = 0
for i in range(3, len(f) - 2, 4):
    if f[i] + f[i+1] + f[i+2] + f[i+3] == 'DBAC':
        cnt += 1
        m = max(m, cnt)
        if m == 23:
            idx = i
    else:
        cnt = 0

print(m*4, idx)
print(f[8205:8220])