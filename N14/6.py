for x in '0123456789A':
    n = int('3364' + x, 11) + int(x + '7946', 12)
    eq = int('55' + x + '87', 14)
    if n == eq:
        print(x, int(f'55{x}87', 14))