f = open('N27_1\\3B.txt')

text = [int(x) for x in f]

k65 = k13 = k5 = k = 0
for i in range(len(text)):
    if text[i] % 65 == 0:
        k65 += 1
    elif text[i] % 13 == 0:
        k13 += 1
    elif text[i] % 5 == 0:
        k5 += 1
    else:
        k += 1

print(k65*(k65-1)//2 + k65*(k+k5+k13) + k13 * k5)