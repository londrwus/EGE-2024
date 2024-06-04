f = open("N17\\17_19.txt")

line = [int(x) for x in f]

max_v = max([x for x in line if abs(x) % 100 == 13])

sp = []
for i in range(len(line) - 2):
    len_3 = len([abs(x) for x in [abs(line[i]), abs(line[i+1]), abs(line[i+2])] if len(str(x)) == 3])
    if len_3 == 2 and (line[i] + line[i+1] + line[i+2]) < max_v:
        sp.append(line[i] + line[i+1] + line[i+2])
        
print(len(sp), min(sp))