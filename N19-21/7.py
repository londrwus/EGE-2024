def f(s, b, m):
    if s + b >= 123:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [
        f(s + 1, b, m - 1),
        f(s, b + 1, m - 1),
        f(s * 2, b, m - 1),
        f(s, b * 2, m - 1),
    ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return any(h)
    
print([s for s in range(1, 110) if not f(13, s, 1) and f(13, s, 2)]) # 28
print([s for s in range(1, 110) if not f(13, s, 1) and f(13, s, 3)]) # 48 54
print([s for s in range(1, 110) if not f(13, s, 2) and f(13, s, 4)]) # 48 54