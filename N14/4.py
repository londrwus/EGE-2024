def conv(num, radix):
    digits = '0123456789'
    final = ''
    while num > 0:
        k = num % radix
        final = digits[k] + final
        num = num // radix
    return final

for x in range(21, 30):
    n = str(conv(x, 3))
    if n[-1] + n[-2] == '11':
        print(x)