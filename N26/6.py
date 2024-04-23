f = open('N26\\6.txt')

text = [int(x) for x in f]
text.sort()

n = 10000

d = {}

for num in text:
    d[num] = d.get(num, 0) + 1

print(len(d), max(d.values()))