f = open('N27_2_dynamic\\8B.txt')

text = [int(x) for x in f]

mn = 0
k0, k0_2, k23, k23_2 = 0, 0, 0, 0
for i in range(len(text)):
    if text[i] % 23 == 0 and text[i] % 2 == 0 and text[i] > k23:
        k23 = text[i]
    if text[i] % 23 == 0 and text[i] % 2 != 0 and text[i] > k23_2:
        k23_2 = text[i]
        
    if text[i] % 2 == 0 and text[i] > k0:
        k0 = text[i]
    if text[i] % 2 != 0 and text[i] > k0_2:
        k0_2 = text[i]
        
    mn = max(k23_2 + k0_2, mn)
    mn = max(k23 + k0, mn)
        
print(mn)