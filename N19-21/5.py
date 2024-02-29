def f(a, b, m):
    if a + b >= 68:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [
        f(a + 1, b, m - 1),
        f(a, b + 1, m - 1),
        f(a + b, b, m - 1),
        f(a, b + a, m - 1),
    ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print([s for s in range(1, 60) if f(s, 8, 2)])  # 18
print([s for s in range(1, 60) if not f(s, 8, 1) and f(s, 8, 3)])  # 17 29
print([s for s in range(1, 60) if not f(s, 8, 2) and f(s, 8, 4)])  # 17 292
