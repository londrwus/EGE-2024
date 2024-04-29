f = open('N27_1\\15B.txt')

text = [int(x) for x in f]

a = [[] for x in range(80)]

for i in range(len(text)):
    ost = text[i] % 80
    a[ost] += [text[i]]

ans = []
for i in range(80):
    if len(a[i]) >= 2:
        ans += [max(a[i]) - min(a[i])]
        
print(max(ans))