f = open('N24_2\\9.txt').readlines()

cnt = 0
for s in f:
    if s.count('S') == s.count('X'):
        cnt += 1

print(cnt)