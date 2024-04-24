f = open('N24\\29.txt').readline().strip()

glas = 'AEIOUY'
sogl = 'BCDFGHJKLMNPQRSTVWXZ'
m = 0
cnt = 1
for i in range(0, len(f) - 1, 2):
    if (f[i] in glas) and (f[i+1] in sogl):
        cnt += 2
        m = max(m, cnt)
    else:
        cnt = 1

print(m)