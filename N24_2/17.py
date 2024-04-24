f = open('N24_2\\17.txt').read().strip()

new = ''
for i in range(len(f) - 2):
    if f[i] == f[i+2]:
        new += f[i+1]

d = {}
for word in new:
    d[word] = d.get(word, 0) + 1

print(d, max(d.values()))