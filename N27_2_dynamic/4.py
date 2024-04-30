f = open('N27_2_dynamic\\4B.txt')

text = [int(x) for x in f]

k = [0] * 131
cnt = 0
for i in range(len(text)):
    if text[i] % 131 == 0:
        ost = 0
    else:
        ost = 131 - text[i] % 131
        
    cnt += k[ost]
    
    k[text[i] % 131] += 1
    
print(cnt)