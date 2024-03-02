f = open("N17\\17_12.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 1):
    if line[i] + line[i+1] >= 100 and (line[i] < 0 or line[i+1] < 0):
        sp.append(line[i] * line[i+1])

print(len(sp), max(sp))