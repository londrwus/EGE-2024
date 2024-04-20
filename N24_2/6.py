f = open('N24_2\\6.txt').read()

cnt = 0
for i in range(len(f)):
    if f[i:i+4] == 'XXXX':
        cnt += 1

print(cnt)