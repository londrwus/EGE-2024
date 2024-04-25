from fnmatch import *

def div(n):
    divs = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(divs)

for x in range(65001, 10**9):
    if fnmatch(str(x), '6*97*5?'):
        if len([i for i in div(x) if i % 2 == 0]) >= 4:
            print(x, sum([i for i in div(x) if i % 2 == 0]))