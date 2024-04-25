def conv(num, radix):
    digits = '0123456789'
    final = ''
    while num > 0:
        k = num % radix
        final = digits[k] + final
        num = num // radix
    return final

s = 5 * 216**1156-4*36**1147+6**1153-875
converted = conv(s, 6)
print(str(converted).count('5') - (str(converted).count('0')))