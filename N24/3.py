f = open('N24\\3.txt').read()
for word in set(f):
    if word.isdigit() == False:
        f = f.replace(f'{word}', ' ')

f = f.split()
print(max(len(c) for c in f))