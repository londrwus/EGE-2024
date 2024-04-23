f = open('N26\\7.txt')

n = 9937
a = [0] * 2_000_001
for i in range(n):
    st, end = map(int, f.readline().split())
    a[st] += 1
    a[end] -= 1

k = 0
st = -1
sp = []
for i in range(2_000_001):
    k0 = k
    k += a[i]
    if k > 0 and st == -1:
        st = i
    if k0 > 0 and (k == 0):
        sp.append(i-st)
        st = -1

print(len(sp), sum(sp))