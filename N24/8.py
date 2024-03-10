f = open('N24\\8.txt').read()
max_v = 0
cnt = 0
for i in range(1, len(f) - 1, 2):
    if f[i] in 'BCD' and f[i+1] in 'AO':
        cnt += 1
        max_v = max(cnt, max_v)
    else:
        cnt = 0

print(max_v)