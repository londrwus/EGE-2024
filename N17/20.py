f = open("N17\\17_20.txt")

ln = [int(x) for x in f]

mx_3 = max([x for x in ln if abs(x) % 10 == 3])

sp = []
for i in range(len(ln) - 1):
    len_3 = len([x for x in [ln[i], ln[i+1]] if abs(x) % 10 == 3])
    if len_3 == 1 and ln[i]**2 + ln[i+1]**2 >= mx_3**2:
        sp.append(ln[i]**2 + ln[i+1]**2)
        
print(len(sp), max(sp))