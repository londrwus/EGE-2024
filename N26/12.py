import math

f = open('N26\\12.txt')

text = [int(x) for x in f]
text.sort()

n = 9604

max_cnt = 0
max_z = 9999999
for i in range(n):
    cnt = 1
    st = text[i]

    for j in range(i + 1, n):
        if math.ceil(st * 1.1) <= text[j]:
            cnt += 1
            st = text[j]

    max_cnt = max(max_cnt, cnt)

    if cnt == 71:
        max_z = min(max_z, st)

print(max_cnt, max_z)