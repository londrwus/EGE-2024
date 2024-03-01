f = open("N17\\17_9.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 2):
    if len([int(x) for x in [line[i], line[i + 1], line[i + 2]] if x % 12 == 0]) >= 1:
        if (
            len([int(x) for x in [line[i], line[i + 1], line[i + 2]] if x % 3 == 0])
            == 3
        ):
            sp.append((line[i] + line[i + 1] + line[i + 2]) / 3)

print(len(sp), min(sp))
