def conv(num, radix):
    digits = "012"
    final = ""
    while num > 0:
        k = num % radix
        final = digits[k] + final
        num = num // radix
    return final


f = open("N17\\17_10.txt")

line = [int(x) for x in f]

sp = []
for i in range(len(line) - 2):
    if (
        len(
            [
                int(x)
                for x in [line[i], line[i + 1], line[i + 2]]
                if str(conv(x, 3))[-1] == "2"
            ]
        )
        >= 1
    ):
        sp.append(min(line[i], line[i + 1], line[i + 2]))

print(len(sp), sum(sp))
