def f(x, y, a):
    return (x**2-10*x+16>0) or (y**2-10*y+21>0) or (x*y<2*a)

for a in range(1, 300):
    if all(f(x, y, a) == 1 for x in range(1, 300) for y in range(1, 300)):
        print(a)