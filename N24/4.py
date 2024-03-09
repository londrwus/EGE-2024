f = open('N24\\4.txt').read()
f = f.replace('XY', 'X Y').replace('XZ', 'X Z')
f = f.split()
print(max(len(c) for c in f))