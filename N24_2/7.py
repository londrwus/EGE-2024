f = open('N24_2\\7.txt').read()

cnt = 0
for i in range(len(f) - 3):
    if f[i] + f[i+2] + f[i+3] == 'GME':
        cnt += 1

print(cnt)