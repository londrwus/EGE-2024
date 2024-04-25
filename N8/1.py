from itertools import *

cnt = 0
for x in permutations('ДЕЙКСТРА', r=6):
    s = ''.join(x)
    s = s.replace('К', 'Д').replace('С', 'Д').replace('Т', 'Д').replace('Р', 'Д')
    if s.count('Й') == 1:
        if (s[0] == 'Й' and s[1] == 'Д'):
            cnt += 5

print(cnt)