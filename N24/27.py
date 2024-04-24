f = open('N24\\27.txt').read()

cnt = 0
m = 0
idx = 0
for i in range(3, len(f) - 2, 3):
    if f[i] + f[i+1] + f[i+2] == 'XYZ':
        cnt += 1
        m = max(m, cnt)
        if cnt == 22:
            idx = i
    else:
        cnt = 0

print(m*3, idx)
print(f[967824-70:967830])