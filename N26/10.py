f = open('N26\\10.txt')

w, n = 9800, 990

text = [int(x) for x in f]
text.sort()

sp = []

for i in range(n):
    cnt = text[i]
    chislo = text[i]
    tries = 1

    for j in range(i + 1, n):
        if text[j] + cnt <= w:
            tries += 1
            chislo = max(chislo, text[j])
            cnt += text[j]
        else:
            sp.append([tries, chislo])
            break

print(sp)