f = open('N27_2_dynamic\\12B.txt')

q = []
text = [int(x) for x in f]

cnt = 0
for i in range(10000):
    for y in q:
        if (text[i] + y) % 8 != 0:
            cnt += 1
    
    q.append(text[i])
    if len(q) > 7:
        q.pop(0)
    
print(cnt)