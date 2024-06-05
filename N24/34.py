f = open('N24\\34.txt').read()
f = f.replace('R', 'Q').replace('W', 'Q').replace('2', '1').replace('4', '1')

cnt = 1
mx_v = 0
for i in range(len(f) - 1):
    if f[i] + f[i+1] != 'QQ' and f[i] + f[i+1] != '11':
        cnt += 1
        mx_v = max(cnt, mx_v)
    else:
        cnt = 1
        
print(mx_v)