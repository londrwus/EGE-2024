f = open("N17\\17_11.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 3):
    if line[i] > line[i+1] > line[i+2] > line[i+3]:
        if line[i] - line[i+3] >= 1000:
            sp.append(line[i] + line[i+1] + line[i+2] + line[i+3])

print(len(sp), min(sp))