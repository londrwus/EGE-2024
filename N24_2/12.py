f = open('N24_2\\11.txt').readlines()

cnt = 0
for s in f:
    if s.count('AOA') > s.count('OAO'):
        cnt += 1

print(cnt)