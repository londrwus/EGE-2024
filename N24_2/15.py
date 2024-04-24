f = open('N24_2\\15.txt').read()

d = {}

for word in f:
    d[word] = d.get(word, 0) + 1

print(max(d.values()))