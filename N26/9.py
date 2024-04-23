f = open('N26\\9.txt')

n = 10000

sp = [[] for x in range(31)]
min_year = 1961
max_year = 1991

for i in range(n):
    year, mark = map(int, f.readline().split())

    if mark not in sp[year-min_year]:
        sp[year-min_year].append(mark)

cnt = 0
for x in range(len(sp)):
    cnt += abs(len(sp[x]) - 8)

print(cnt)