f = open('N27_1\\9B.txt')

text = [int(x) for x in f]

a = [0] * 2000

for i in range(len(text)):
    ost = text[i] % 2000
    if text[i] <= 1999:
        a[ost] += 1
        
cnt = a[1000]*(a[1000]-1)//2
for i in range(1, 1000):
    cnt += a[i]*a[2000-i]
    
print(cnt)