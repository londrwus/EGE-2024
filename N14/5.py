for x in '0123456789ABCDE':
    n = int('123' + x + '5', 15) + int('1' + x + '233', 15)
    if n % 14 == 0:
        print(n // 14)