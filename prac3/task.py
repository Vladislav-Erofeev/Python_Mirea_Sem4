def main(m, b):
    a = 0
    for c in range(1, m+1):
        a += 71 - c ** 5
    c = 0
    for i in range(1, m+1):
        for k in range(1, b+1):
            c += (14 * i ** 2) + (k ** 2 + 39 * i + 0.02) ** 3 + 86 * i ** 4
    return a - c


print(main(8, 8))
