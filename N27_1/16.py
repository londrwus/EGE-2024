f = open('N27_1\\16B.txt')

text = [int(x) for x in f]

d = {}
for i in range(len(text)):
    cnt = sum(int(c) for c in str(text[i]))
    d[cnt] = d.get(cnt, 0) + 1
    
print(max(d.values()))