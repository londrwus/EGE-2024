f = open('N9\\5.txt')

cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    cnt_3 = [x for x in a if a.count(x) == 3]
    cnt_1 = [x for x in a if a.count(x) == 1]
    if len(cnt_3) == 3 and len(cnt_1) == 3:
        if sum(cnt_3) >= sum(cnt_1) / 3:
            cnt += 1

print(cnt)