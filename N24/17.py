f = open('N24\\17.txt').read()

cnt = 0
max_v = 0 # 15; 
for i in range(2, len(f) - 2, 3):
    if (f[i] == 'A' and f[i + 2] == 'A') or (f[i] == 'C' and f[i + 2] == 'C'):
        cnt += 1
        max_v = max(max_v, cnt)
    else:
        cnt = 0

print(max_v)