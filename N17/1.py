f = open("N17\\17_1.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line)):
    if (
        line[i] % 3 == 0
        and line[i] % 7 != 0
        and line[i] % 17 != 0
        and line[i] % 19 != 0
        and line[i] % 27 != 0
    ):
        sp.append(line[i])

print(len(sp), max(sp))
