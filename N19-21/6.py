def f(a, b, m):
    if a * b >= 63:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [
        f(a + 1, b, m - 1),
        f(a, b + 1, m - 1),
        f(a * 2, b, m - 1),
        f(a, b * 2, m - 1),
    ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print([s for s in range(1, 32) if f(s, 2, 2)])  # 18
print([s for s in range(1, 32) if not f(s, 2, 1) and f(s, 2, 3)])  # 7 14
print([s for s in range(1, 32) if not f(s, 2, 2) and f(s, 2, 4)])  # 7 14
