s = 6*144**26+11*12**75-48

def conv(num, radix):
    digits = '0123456789' + 'AB'
    final = ''
    while num > 0:
        k = num % radix
        final = digits[k] + final
        num = num // radix
    return final

print(str(conv(s, 12)).count('B'))