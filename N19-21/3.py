def f(s, b, m):
    if s + b >= 59:
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


print([s for s in range(1, 53) if f(s, 5, 1)])  # 27
print([s for s in range(1, 53) if not f(s, 5, 1) and f(s, 5, 3)])  # 24 26
print([s for s in range(1, 53) if not f(s, 5, 2) and f(s, 5, 4)])  # 23
