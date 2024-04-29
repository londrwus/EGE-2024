f = open('N27_1\\17B.txt')

text = [int(x) for x in f]

d = {}
for i in range(len(text)):
    cnt = str(text[i])[0]
    d[cnt] = d.get(cnt, 0) + 1
    
print(min(d.values()))