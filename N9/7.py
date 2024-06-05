f = open('N9\\7.txt')

cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    len_0 = len([int(x) for x in a if x % 2 == 0])
    len_1 = len([int(x) for x in a if x % 2 != 0])
    if len_1 > 0 and len_0 > 0:
        if len_1 % 2 != 0 and len_0 % 2 == 0:
            mx_amn = max([int(x) for x in a if x % 2 == 0])
            if mx_amn % 4 == 0:
                cnt += 1
                
print(cnt)