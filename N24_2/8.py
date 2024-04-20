f = open('N24_2\\8.txt').read()

cnt = 0
for i in range(len(f) - 4):
    if f[i] + f[i+2] + f[i+4] == 'AAA':
        cnt += 1

print(cnt)