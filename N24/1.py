f = open('N24\\1.txt').read()
f = f.replace('C', ' ').replace('D', ' ')
f = f.split()
print(max(len(c) for c in f))