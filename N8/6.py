from itertools import *

cnt = 0
for x in product('0123456', repeat=7):
    s = ''.join(x)
    if s[0] != '0':
        if len([str(j) for j in s if int(j) % 2 == 0]) == 2:
            cnt += 1
        
print(cnt)