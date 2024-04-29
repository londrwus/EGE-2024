f = open('N27_1\\18B.txt')

text = [int(x) for x in f]

d = {}
for i in range(len(text)):
    for num in str(text[i]):
        d[num] = d.get(num, 0) + 1
        
print(min(d.values()))