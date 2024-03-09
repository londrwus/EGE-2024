f = open('N24\\6.txt').read()
f = f.replace('XZZY', 'XZZ ZZY')
f = f.split()
print(max(len(c) for c in f))