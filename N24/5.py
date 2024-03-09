f = open('N24\\5.txt').read()
f = f.replace('PP', 'P P')
f = f.split()
print(max(len(c) for c in f))