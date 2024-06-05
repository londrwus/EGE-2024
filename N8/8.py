from itertools import *

cnt = 0
for x in permutations('0123456789ABCDEF', r=3):
    s = ''.join(x)
    if s[0] != '0':
        for c in '2468ACE':
            s = s.replace(c, '0')
        for j in '13579BDF':
            s = s.replace(j, '1')
            
        if '00' not in s and '11' not in s:
            cnt += 1
            
print(cnt)