f = open('N24\\25.txt').read()

max_v = 0
cnt = 0
for i in range(0, len(f), 2):
    if f[i] + f[i+1] == 'CA':
        cnt += 1
        max_v = max(max_v, cnt)
    else:
        cnt = 0
    
print(max_v*2)