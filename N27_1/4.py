f = open('N27_1\\4B.txt')

text = [int(x) for x in f]

k5 = k = k2 = k10 = 0
for i in range(len(text)):
    if text[i] % 5 == 0 and text[i] % 2 == 0:
        k5 += 1
    if text[i] % 5 != 0 and text[i] % 2 == 0:
        k += 1
    if text[i] % 5 == 0 and text[i] % 2 != 0:
        k10 += 1
    if text[i] % 5 != 0 and text[i] % 2 != 0:
        k2 += 1
        
print(k5 * k10 + k5 * k2 + k * k10)