def main(z):
    a = 19 * z ** 2 + 1 + z ** 4
    b = z + 20 * z ** 3 + (abs(60 * z ** 3 - 71 - z / 87)) ** 2
    c = z ** 3
    if z < 27:
        return a
    elif 27 <= z < 97:
        return b
    else:
        return c
