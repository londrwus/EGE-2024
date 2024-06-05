f = open('N27_2_dynamic\\6B.txt')

text = [int(x) for x in f]

mx = 0
b, c = 0, 0
for i in range(len(text)):
    if text[i] % 2 == 0:
        mx = max(text[i] + b, mx)
    else:
        mx = max(text[i] + c, mx)
        
    if text[i] % 2 == 0 and text[i] > c:
        c = text[i]
    if text[i] % 2 != 0 and text[i] > b:
        b = text[i]
    
print(mx)