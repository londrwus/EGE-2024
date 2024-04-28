f = open('N27_1\\7B.txt')

text = [int(x) for x in f]
a = [0] * 69
for i in range(len(text)):
    ost = text[i] % 69
    a[ost] += 1
    
cnt = 0
for i in range(69):
    cnt += a[i]*(a[i]-1)//2
    
print(cnt)