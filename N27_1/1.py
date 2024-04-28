f = open('N27_1\\1B.txt')

text = [int(x) for x in f]

k0 = k1 = 0
for i in range(len(text)):
    if text[i] % 2 == 0:
        k0 += 1
    else:
        k1 += 1

print(k0*(k0-1)//2+k1*(k1-1)//2)