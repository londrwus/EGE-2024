f = open("N17\\17_15.txt")

line = [int(x) for x in f]
del_19 = max([i for i in line if i % 19 == 0])
sp = []
for i in range(len(line) - 1):
    if line[i] > del_19 or line[i+1] > del_19:
        sp.append(line[i] + line[i+1])

print(len(sp), min(sp))