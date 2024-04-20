f = open('N24_2\\1.txt').read()

cnt = 0
for i in range(len(f)):
    if f[i:i+5] == 'XVIII':
        cnt += 1

print(cnt)