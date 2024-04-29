f = open('N27_1\\10B.txt')

text = [int(x) for x in f]

a_chet = []
a_nechet = []

for i in range(len(text)):
    if text[i] % 2 == 0:
        a_chet += [text[i]]
    else:
        a_nechet += [text[i]]
        
a_chet.sort()
a_nechet.sort()
        
print(a_chet[-1]+a_nechet[-1])