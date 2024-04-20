f = open('N24_2\\10.txt').readlines()

cnt = 0
for s in f:
    if s.count('B') >= s.count('A') * 1.05:
        cnt += 1

print(cnt)