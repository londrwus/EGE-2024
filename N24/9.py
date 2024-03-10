f = open('N24\\9.txt').read()
cnt = 0
max_v = 0
for i in range(0, len(f) - 2, 3):
    if f[i] in '12' and f[i+1] in '12' and f[i+2] in 'AB':
        cnt += 1
        max_v  = max(cnt, max_v)
    else:
        cnt = 0

print(max_v)