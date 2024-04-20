f = open('N24\\16.txt').read()

f = f.replace('PC', '**').replace('CSGO', '****')

cnt = 0
max_v = 0
for i in range(len(f)):
    if f[i] == '*':
        cnt += 1
        max_v = max(max_v, cnt)
    else:
        cnt = 0

print(max_v)