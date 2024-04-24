f = open('N24_2\\18.txt').read()

d = {}
s = ''
for i in range(len(f) - 4):
    if f[i] + f[i+1] == 'CB' and f[i+3] + f[i+4] == 'BC':
        s += f[i+2]

for word in s:
    d[word] = d.get(word, 0) + 1

print(d, max(d.values()))