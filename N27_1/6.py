f = open('N27_1\\6B.txt')

text = [int(x) for x in f]
a = [0] * 131
for i in range(len(text)):
    ost = text[i] % 131
    a[ost] += 1
    
cnt = a[0]*(a[0]-1)//2
for i in range(1, 66):
    cnt += a[i] * a[131-i]
    
print(cnt)