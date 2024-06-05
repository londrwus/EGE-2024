f = open('N27_2_dynamic\\7B.txt')

text = [int(x) for x in f]

mn = 999999999
k0, k31 = 999999999, 999999999
for i in range(len(text)):
    mn = min(k31 * k0, mn)
    
    if text[i] % 31 == 0 and text[i] < k31:
        k31 = text[i]
    if text[i] % 31 != 0 and text[i] < k0:
        k0 = text[i]
        
print(mn)