f = open('N27_1\\13B.txt')

text = [int(x) for x in f]

a = [[] for x in range(11)]

for i in range(len(text)):
    ost = text[i] % 11
    a[ost] += [text[i]]
    
final = []
for i in range(11):
    a[i].sort()
    final += a[i][:3]
    
final.sort()
ans = []
for i in range(len(final)):
    for j in range(i + 1, len(final)):
        for k in range(j + 1, len(final)):
            if (final[i] + final[j] + final[k]) % 11 == 0:
                ans.append(final[i] + final[j] + final[k])
                
print(min(ans))