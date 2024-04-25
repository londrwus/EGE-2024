from itertools import *

cnt = 0
for x in permutations('ВАЙФУ', r=4):
    s = ''.join(x)
    if s[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
        cnt += 1

print(cnt)