f = open('N26\\8.txt')

# 222500000 1500 1000

L, M, N = map(int, f.readline().split())

a2 = sorted([list(map(int, x.split())) for x in f])
print(a2)

a = [[0,0]] + a2 + [[L,0]]

res = []

for i in range(1, len(a)):
    l = a[i][0] - (a[i-1][0] + a[i-1][1])
    if l >= M: 
        res.append(l)

print(len(res), max(res))