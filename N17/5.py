def conv(num, radix):
    digits = "0123456789ABCDEF"

    final = ""
    while num > 0:
        k = num % radix
        final = digits[k] + final
        num = num // radix

    return final


f = open("N17\\17_5.txt")
line = [int(x) for x in f]
sp = []

for i in range(len(line)):
    if str(conv(line[i], 16))[-1] == "B":  # or just line[i] % 16 == 11
        if (
            line[i] % 7 == 0
            and line[i] % 6 != 0
            and line[i] % 13 != 0
            and line[i] % 19 != 0
        ):
            sp.append(line[i])

print(sum(sp), len(sp))
