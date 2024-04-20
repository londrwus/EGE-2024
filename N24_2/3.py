f = open('N24_2\\3.txt').read()

f = f.replace("STOCK", '*')

cnt = 0
for i in range(len(f)):
    if f[i:i+3] == 'OCK':
        cnt += 1

print(cnt)