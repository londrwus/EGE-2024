f = open('N27_2_dynamic\\13B.txt')

q = [int(f.readline()) for i in range(5)]
text = [int(x) for x in f]

k = [[0]*13 for i in range(2)]

cnt = 0
for i in range(10000 - 5):
    ost = text[i] % 13
    
    if text[i] % 2 == 0:
        cnt += k[0][ost] + k[1][ost]
    if text[i] % 2 != 0:
        cnt += k[0][ost]
    
    k[q[0]%2][q[0]%13] += 1
    
    q.append(text[i])
    q.pop(0)
    
print(cnt)