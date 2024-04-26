f = open("N17\\17_16.txt")

line = [int(x) for x in f]
krat_11 = len([i for i in line if i % 11 == 0])
sp = []
for i in range(len(line)):
    if line[i] % 11 == 0:
        sp.append(line[i])

print(len(sp), min(sp))