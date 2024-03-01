f = open("N17\\17_8.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 2):
    if (line[i] * line[i + 1] * line[i + 2]) % 7 == 0 and (
        line[i] + line[i + 1] + line[i + 2]
    ) % 10 == 5:
        sp.append(line[i] + line[i + 1] + line[i + 2])

print(len(sp), max(sp))
