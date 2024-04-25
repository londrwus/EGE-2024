from itertools import *

cnt = 0
for x in product('ЕЛМРУ', repeat=4):
    s = ''.join(x)
    cnt += 1
    if s[0] == 'Л':
        print(cnt)