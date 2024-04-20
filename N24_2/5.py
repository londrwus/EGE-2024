f = open('N24_2\\5.txt').read()

cnt = 0
for i in range(len(f)):
    if f[i:i+3] == 'XIX':
        cnt += 1

print(cnt)