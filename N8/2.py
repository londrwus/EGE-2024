from itertools import *

cnt = 0
for x in permutations('ИГРОК', r=5):
    s = ''.join(x)
    if s[0] != 'К' and 'РОК' not in s:
        cnt += 1

print(cnt)