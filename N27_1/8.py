f = open('N27_1\\8B.txt')

text = [int(x) for x in f]

a = [0] * 80
b = [0] * 80

for i in range(len(text)):
    ost = text[i] % 80
    if text[i] > 50000:
        b[ost] += 1
    else:
        a[ost] += 1
        
cnt = b[0]*(b[0] - 1)//2 + b[40]*(b[40]-1)//2
for i in range(1, 40):
    cnt += b[i]*b[80-i]
    
cnt += b[0]*a[0] + b[40]*a[40]
for i in range(1, 40):
    cnt += a[i]*b[80-i]
    cnt += b[i]*a[80-i]
    
print(cnt)