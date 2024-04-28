f = open('N27_1\\2B.txt')

text = [int(x) for x in f]

k0 = k1 = 0
for i in range(len(text)):
    if text[i] % 7 == 0:
        k0 += 1
    else:
        k1 += 1

print(k0*(k0-1)//2+k0*k1)