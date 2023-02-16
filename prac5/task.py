def main(y):
    ans = 0
    for i in range(1, len(y)+1):
        ans += (y[i-1] ** 2 + 39 * y[i-1] + 0.02) ** 6
    return ans

print(main([0.21, 0.65, -0.91, -0.08, 0.47, -0.73]))
