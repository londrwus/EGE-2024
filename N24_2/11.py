f = open('N24_2\\11.txt').readlines()

cnt = 0
for s in f:
    for i in range(len(s) - 3):
        if s[i] + s[i+2] + s[i+3] == 'KGE':
            cnt += 1
            break

print(cnt)