f = open('N27_1\\11B.txt')

text = [int(x) for x in f]

a31 = []
a = []

for i in range(len(text)):
    if text[i] % 31 == 0:
        a31 += [text[i]]
    else:
        a += [text[i]]
        
a31.sort()
a.sort()

print(min(a31[0]*a[0], a31[0]*a31[1]))