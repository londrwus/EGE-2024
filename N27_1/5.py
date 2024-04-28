f = open('N27_1\\5B.txt')

text = [int(x) for x in f]

cnt = 0
for i in range(len(text)):
    if text[i] % 19 == 0:
        cnt += 1
        
print((cnt*(cnt-1)*(cnt-2))//6)