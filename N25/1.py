from fnmatch import *

for x in range(0, 10**9, 17):
    if fnmatch(str(x), '12345?6?8'):
        print(x, x // 17)