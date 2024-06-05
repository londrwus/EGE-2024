f = open('N27_2_dynamic\\11B.txt')

q = [int(f.readline()) for i in range(5)]
text = [int(x) for x in f]

k1, k3, k7, k9, cnt = 0, 0, 0, 0, 0
for i in range(10000 - 5):
    if text[i] % 10 == 1:
        cnt += k3
    if text[i] % 10 == 3:
        cnt += k1
    if text[i] % 10 == 9:
        cnt += k7
    if text[i] % 10 == 7:
        cnt += k9
        
    if q[0] % 10 == 1:
        k1 += 1
    if q[0] % 10 == 3:
        k3 += 1
    if q[0] % 10 == 7:
        k7 += 1
    if q[0] % 10 == 9:
        k9 += 1
    
    q.append(text[i])
    q.pop(0)
    
print(cnt)