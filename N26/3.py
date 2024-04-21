f = open('N26\\3.txt')

n, weight = 1000, 600

text = [int(x) for x in f]
text.sort()

sp = [[] for x in range(1000)]

cnt = 0
while len(text) > 0:
    for i in range(len(sp)):
        for j in range(len(text) - 1, -1, -1):
            if sum(sp[i]) + text[j] <= weight:
                sp[i] += [text[j]]
                text.remove(text[j])

sp = [x for x in sp if x != []]

print(len(sp), sum(sp[-1]))