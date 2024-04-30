f = open('N27_2_dynamic\\1B.txt')

text = [int(x) for x in f]

k0 = k7 = 0
cnt = 0
for i in range(len(text)):
    if text[i] % 7 == 0:
        cnt += k0
    else:
        cnt += k7
        
    k0 += 1
    if text[i] % 7 == 0:
        k7 += 1
        
print(cnt)