f = open('N27_2_dynamic\\5B.txt')

text = [int(x) for x in f]

a = [0] * 80
b = [0] * 80
cnt = 0

for i in range(len(text)):
    if text[i] % 80 == 0:
        ost = 0
    else:
        ost = 80 - text[i] % 80
    
    if text[i] > 50000:
        cnt += a[ost]
    else:
        cnt += b[ost]
        
    #print(text[i], a, b)
        
    a[text[i] % 80] += 12
    if text[i] > 50000:
        b[text[i] % 80] += 1
        
print(cnt)