f = open('N24\\32.txt').read().strip()

l = 0
fx = 0
m = 0
for i in range(1, len(f)):
    if f[i-1] + f[i] == 'AB': fx += 1

    while fx > 50:
        if f[l] + f[l+1] == 'AB': fx -= 1
        l += 1

    if fx == 50:
        m = max(m, i - l + 1)

print(m)