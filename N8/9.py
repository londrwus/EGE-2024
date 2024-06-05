from itertools import *

cnt = 0
sp = []
for x in product('ЕКМОПРТЬЮ', repeat=5):
    s = ''.join(x)
    cnt += 1
    if cnt % 2 != 0 and s.count('К') == 2 and s[0] != 'Ь':
        sp.append(cnt)
        
print(max(sp))