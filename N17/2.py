f = open("N17\\17_2.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line)):
    if str(line[i])[-1] == "2" or str(line[i])[-1] == "7":
        if line[i] % 3 == 0 and line[i] % 11 == 0:
            sp.append(line[i])

print(len(sp), min(sp))
