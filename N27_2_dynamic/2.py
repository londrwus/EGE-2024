f = open('N27_2_dynamic\\2B.txt')

text = [int(x) for x in f]

all_pairs = pairs5 = pairs13 = pairs65 = 0
cnt = 0

for i in range(len(text)):
    if text[i] % 65 == 0:
        cnt += all_pairs
    elif text[i] % 13 == 0:
        cnt += pairs5
    elif text[i] % 5 == 0:
        cnt += pairs13
    else:
        cnt += pairs65
    
    all_pairs += 1
    if text[i] % 65 == 0:
        pairs65 += 1
    if text[i] % 13 == 0:
        pairs13 += 1
    if text[i] % 5 == 0:
        pairs5 += 1
        
print(cnt)