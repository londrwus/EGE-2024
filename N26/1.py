f = open('N26\\1.txt')

s, n = map(int, f.readline().split())

text = [int(x) for x in f]
text.sort()

b = []
while sum(b) + text[0] <= s:
    for i in range(len(text) - 1, 0, -1):
        if sum(b) + text[i] <= s:
            b += [text.pop(i)]
            break
    
    if sum(b) + text[0] <= s:
        b += [text.pop(0)]

print(len(b), b[-1])