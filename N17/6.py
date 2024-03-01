f = open("N17\\17_6.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 1):
    summe = abs(line[i] + line[i + 1])
    if summe % 3 == 0 and summe % 6 != 0:
        if abs(line[i] * line[i + 1]) % 10 == 8:
            sp.append(line[i] + line[i + 1])

print(len(sp), max(sp))
