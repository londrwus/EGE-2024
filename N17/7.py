f = open("N17\\17_7.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 1):
    if (line[i] * line[i + 1]) > 0:
        if (line[i] + line[i + 1]) % 7 == 0:
            sp.append(line[i] * line[i + 1])

print(len(sp), min(sp))
