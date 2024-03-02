f = open("N17\\17_13.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 1):
    if abs(line[i]) + abs(line[i+1]) < 200 and abs(line[i]) + abs(line[i+1]) > 50:
        sp.append(min(line[i], line[i+1]))

print(len(sp), min(sp))