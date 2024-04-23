f = open('N26\\11.txt')

n = 10000

text = [int(x) for x in f]
text.sort()

max_v = 0
max_cnt = 0
sp = []
for i in range(n):
    cnt = 1
    st = text[i]

    for j in range(i + 1, n):
        if abs(st - text[j]) >= 8:
            cnt += 1
            st = text[j]

    max_cnt = max(max_cnt, cnt)

    if cnt == 1198:
        max_v = max(max_v, text[i])

print(max_cnt, max_v)