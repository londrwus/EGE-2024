f = open('N26\\2.txt')

s = 6666

text = [int(x) for x in f]
text.sort()

f_file = []
s_file = []

while len(f_file) + len(s_file) < s:
    if sum(f_file) > sum(s_file):
        s_file.append(text[0])
        text.pop(0)

    if sum(f_file) <= sum(s_file) and len(text) > 0:
        f_file.append(text[-1])
        text.pop(-1)

print(len(f_file), len(s_file))