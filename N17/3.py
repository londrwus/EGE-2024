f = open("N17\\17_3.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line)):
    if line[i] % 10 == 5 or line[i] % 10 == 7:
        if line[i] % 9 != 0 and line[i] % 11 != 0:
            sp.append(line[i])

print(len(sp), min(sp) + max(sp))
