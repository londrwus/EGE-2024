f = open('N24\\24.txt').read()


cnt = 0
m = 99999
l = 0
for i in range(2, len(f)):
    if f[i-2] + f[i-1] + f[i] == 'BAD' or f[i-2] + f[i-1] + f[i] == 'FAT':
        cnt += 1

    while cnt == 3:
        m = min(m, i - l + 1)
        if f[l] + f[l+1] + f[l+2] == 'BAD' or f[l] + f[l+1] + f[l+2] == 'FAT': 
            cnt -= 1
        l += 1

print(m)