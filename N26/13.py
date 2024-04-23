f = open('N26\\13.txt')

n = 15186
a = [0] * 1000

sp = []

min_v = 32

for i in range(n):
    id, date, h, duration = map(int, f.readline().split())

    for i in range(duration+1):
        a[date*24+h+i] += 1

    a[date*24+h+duration] -= 1

    if a[date*24+h+duration] == 161:
        min_v = min(min_v, date)

print(max(a), min_v)