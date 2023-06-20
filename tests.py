array = []
for x in range(158):
    num1 = 2*158**4 + 7*158**3 + 3*158**2 + x*158**1 + 2*158**0
    num2 = 1*158**4 + x*158**3 + 3*158**2 + 9*158**1 + 0*158**0

    if (num1 + num2) % 73 == 0:
        array.append((num1 + num2) // 73)

print(sum(array))