f = open("N17\\17_17.txt")

line = [int(x) for x in f]
s = max([x for x in line if x % 10 == 4]) + min([x for x in line if x % 10 == 4])
sp = []
for i in range(len(line) - 1):
    if line[i] + line[i + 1] < s:
        sp.append(line[i] + line[i + 1])

print(len(sp), max(sp))