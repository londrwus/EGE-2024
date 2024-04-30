f = open('N27_2_dynamic\\3B.txt')

text = [int(x) for x in f]

pairs0 = pairs5 = pairs2 = pairs10 = 0
cnt = 0
for i in range(len(text)):
    if text[i] % 5 == 0 and text[i] % 2 == 0:
        cnt += pairs0
    if text[i] % 5 == 0 and text[i] % 2 != 0:
        cnt += pairs2
    if text[i] % 5 != 0 and text[i] % 2 == 0:
        cnt += pairs5
    if text[i] % 5 != 0 and text[i] % 2 != 0:
        cnt += pairs10
        
    if text[i] % 5 == 0 and text[i] % 2 == 0:
        pairs10 += 1
    if text[i] % 5 == 0 and text[i] % 2 != 0:
        pairs5 += 1
    if text[i] % 2 == 0:
        pairs2 += 1
    if text[i] % 2 != 0:
        pairs0 += 1
        
print(cnt)