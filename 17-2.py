amount = 0
mx = 0
#делятся на 6 и не делятся на 7, 13, 17 и 23
for i in range(1100, 11000 + 1):
    if i % 6 == 0 and i % 7 != 0 and i % 13 != 0 and i % 23 != 0 and i % 17 != 0:
        amount += 1
        mx = i
print(amount, mx)