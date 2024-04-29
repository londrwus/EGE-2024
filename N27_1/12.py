f = open('N27_1\\12B.txt')

text = [int(x) for x in f]

a23 = []
a23_2 = []
a2 = []
a = []

for i in range(len(text)):
    ost = text[i] % 23
    if ost == 0 and text[i] % 2 == 0:
        a23 += [text[i]]
    if ost == 0 and text[i] % 2 != 0:
        a23_2 += [text[i]]
    if ost != 0 and text[i] % 2 == 0:
        a2 += [text[i]]
    if ost != 0 and text[i] % 2 != 0:
        a += [text[i]]

a23.sort()
a23_2.sort()
a2.sort()
a.sort()

m = a23[-2:] + a23_2[-2:] + a2[-2:] + a[-2:]
ans = []
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if ((m[i]*m[j]) % 23 == 0) and (m[i]+m[j]) % 2 == 0:
            ans.append(m[i]+m[j])
            
print(max(ans))