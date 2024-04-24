f = open('N24_2\\13.txt').readline()

cnt = 0
for i in range(len(f) - 6):
    if f[i] == 'A' and f[i+6] == 'F':
        cnt += 1

for i in range(len(f) - 7):
    if f[i] == 'A' and f[i+7] == 'F':
        cnt += 1

for i in range(len(f) - 8):
    if f[i] == 'A' and f[i+8] == 'F':
        cnt += 1

for i in range(len(f) - 9):
    if f[i] == 'A' and f[i+9] == 'F':
        cnt += 1

print(cnt)