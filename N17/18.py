f = open("N17\\17_18.txt")

line = [int(x) for x in f]

sp = []
max_v = max([j for j in line if abs(j) % 100 == 21])
for i in range(len(line) - 1):
    if ((len(str(abs(line[i]))) == 5 and str(abs(line[i]))[-2:] == '21') != (len(str(abs(line[i+1]))) == 5 and str(abs(line[i+1]))[-2:] == '21')):
        if (line[i])**2 + (line[i+1])**2 > max_v**2:
            sp.append(line[i] + line[i+1])
        
print(len(sp), max(sp))