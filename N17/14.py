f = open("N17\\17_14.txt")

line = [int(x) for x in f]

sp = []
sr_ar = sum(line) / len(line)
for i in range(len(line) - 2):
    if (line[i] > sr_ar) + (line[i+1] > sr_ar) + (line[i+2] > sr_ar) >= 2:
        sp.append(line[i] + line[i+1] + line[i+2])

print(len(sp), max(sp))