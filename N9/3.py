f = open('N9\\3.txt')

cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if (a[0] + a[2] == a[1] + a[3]) or (a[0] + a[3] == a[1] + a[2]) or (a[0] + a[1] == a[2] + a[3]):
        if (a[3] - a[0]) < (a[1] + a[2] - a[3]):
            cnt += 1

print(cnt)