f = open('N26\\5.txt')

text = [int(x) for x in f]
text.sort()

b = set(text)
sp = []
n = 5000

for i in range(n):
    for j in range(i + 1, n):
        if text[i] % 2 != text[j] % 2:
            if (text[i] + text[j]) in b:
                sp.append(text[i] + text[j])

print(len(sp), max(sp))