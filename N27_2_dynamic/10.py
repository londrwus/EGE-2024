f = open('N27_2_dynamic\\10B.txt')

q = [int(f.readline()) for i in range(4)]
text = [int(x) for x in f]

k13, k0, k13_2, k0_2, cnt = 0, 0, 0, 0, 0
for i in range(10000 - 4):
    if text[i] % 13 == 0 and text[i] % 2 == 0:
        cnt += k0_2
    if text[i] % 13 == 0 and text[i] % 2 != 0:
        cnt += k0
    if text[i] % 13 != 0 and text[i] % 2 == 0:
        cnt += k13_2
    if text[i] % 13 != 0 and text[i] % 2 != 0:
        cnt += k13
    
    if q[0] % 13 == 0 and q[0] % 2 == 0:
        k13 += 1
    if q[0] % 13 == 0 and q[0] % 2 != 0:
        k13_2 += 1
    if q[0] % 2 == 0:
        k0 += 1
    if q[0] % 2 != 0:
        k0_2 += 1
    
    q.append(text[i])
    q.pop(0)
    
print(cnt)