f = open('N27_1\\14B.txt')

text = [int(x) for x in f]

a = [[] for x in range(12)]

for i in range(len(text)):
    ost = text[i] % 12
    a[ost] += [text[i]]
    
final = []
for i in range(12):
    a[i].sort()
    final += a[i][-4:]

final.sort()

ans = []
for i in range(len(final)):
    for j in range(i + 1, len(final)):
        for k in range(j + 1, len(final)):
            for x in range(k + 1, len(final)):
                if (final[i] * final[j] * final[k] * final[x]) % 12 == 0:
                    ans.append(final[i] + final[j] + final[k] + final[x])
                    
print(max(ans))