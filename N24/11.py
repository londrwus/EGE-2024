f = open('N24\\11.txt').read()
f = f.replace('XYX', ' ').replace('ZYZ', ' ').replace('YXY', ' ').replace('ZXZ', ' ').replace('XZX', ' ').replace('YZY', ' ').replace('XXX', ' ').replace('YYY', ' ').replace('ZZZ', ' ')
f = f.split()
print(max(len(c) for c in f))