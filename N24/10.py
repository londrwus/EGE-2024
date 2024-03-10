f = open('N24\\10.txt').read()
f = f.replace('P', 'N').replace('O', 'N')

while 'NN' in f:
    f = f.replace('NN', 'N N')

f = f.split()

print(max(len(c) for c in f))