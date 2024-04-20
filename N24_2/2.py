f = open('N24_2\\2.txt').read()

cnt = 0
for i in range(len(f)):
    if f[i:i+3] == 'TIK' or f[i:i+3] == 'TOK':
        cnt += 1

print(cnt)