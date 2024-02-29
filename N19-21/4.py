def f(s, b, m):
    if s + b >= 77:
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
        return all(h)


print([s for s in range(1, 70) if f(s, 7, 2)])  # 18
print([s for s in range(1, 70) if f(s, 7, 3)])  # 31 34
print([s for s in range(1, 70) if not f(s, 7, 2) and f(s, 7, 4)])  # 30
