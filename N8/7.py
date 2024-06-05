from itertools import *

cnt = 0
for x in product('АКЛОШ', repeat=5):
    cnt += 1
    s = ''.join(x)
    if s == 'ШАЛАШ':
        print(cnt)