f = open('N27_2_dynamic\\9B.txt')

q = [int(f.readline()) for i in range(8)]
text = [int(x) for x in f]

k23, k0, cnt = 0, 0, 0
for i in range(10000 - 8):
    if text[i] % 23 == 0:
        cnt += k0
    else:
        cnt += k23
        
    k0 += 1
    if q[0] % 23 == 0:
        k23 += 1
    
    q.append(text[i])
    q.pop(0)
    
print(cnt)