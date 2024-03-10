f = open('N24\\7.txt').read()
f = f.replace('NPO', '*').replace('PNO', '*').replace('N', ' ').replace('P', ' ').replace('O', ' ')
f = f.split()
print(max(len(c) for c in f))