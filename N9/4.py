f = open('N9\\4.txt')

cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if a[3] - a[0] >= 50:
        if a[1] * a[2] <= 1000:
            cnt += 1

print(cnt)