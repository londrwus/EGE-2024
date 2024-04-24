f = open('N24_2\\18.txt').readlines()

sp = []
for line in f:
    d = {}
    for word in line:
        d[word] = d.get(word, 0) + 1

    for value, key in enumerate(d.items()):
        print(value, key)