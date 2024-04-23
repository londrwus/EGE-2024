f = open('N26\\4.txt')

text = [int(x) for x in f]
text.sort()

n = 5000

sp = []
for i in range(n):
    for j in range(i+1, n):
        if (text[i] + text[j]) % 2 == 0:
            sr = (text[i] + text[j]) // 2
            if text[2499] < sr < text[3750]:
                sp.append(sr)

print(len(sp), min(sp))