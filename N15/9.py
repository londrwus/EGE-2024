p = [i for i in range(2, 21, 2)]
q = [i for i in range(5, 51, 5)]
a = [i for i in range(100)]

for i in range(100):
    for x in range(1000):
        if (((x == i) <= (x in p)) and ((x in q) <= (x != i))) == 0:
            a.remove(i)
            
print(len(a))