f = open("N17\\17_4.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line)):
    if line[i] % 13 == 7:
        if line[i] % 11 != 0 and line[i] % 7 != 0:
            sp.append(line[i])

print(max(sp) - min(sp), len(sp))
