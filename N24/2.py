f = open('N24\\2.txt').read()
f = f.replace('A', ' ').replace('B', ' ').replace('C', ' ')
f = f.split()
print(max(len(c) for c in f))