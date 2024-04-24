f = open('N24\\33.txt').read().strip()

m = 0
cnt = 0
for i in range(0, len(f), 2):
    if (f[i] in '6789') and (f[i+1] not in '6789'):
        cnt += 2
        m = max(m, cnt)
    else:
        cnt = 0

print(m)