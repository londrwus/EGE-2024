f = open('N24_2\\16.txt').read().strip()

d = {}
for word in f:
    d[word] = d.get(word, 0) + 1

print(max(d.values()) - min(d.values()))