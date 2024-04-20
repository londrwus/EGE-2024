f = open('N9\\1.txt')

cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if a[0] + a[3] < a[1] + a[2]:
        cnt += 1

print(cnt)