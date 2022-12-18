# 123x5 + 1x233
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
for x in range(15):
    a = [1, 2, 3, x, 5]
    b = [1, x, 2, 3, 3]

    a.reverse()
    b.reverse()
    # 5 * 15^0 + x * 15^1 + 3 * 15^2 + 2 * 15^3 + 1 * 15^4

    sum_a = 0
    sum_b = 0
    for i in range(5):
        sum_a += a[i] * 15 ** i
        sum_b += b[i] * 15 ** i

    if (sum_a + sum_b) % 14 == 0:
        print(x)
        print((sum_a + sum_b) // 14)
        break