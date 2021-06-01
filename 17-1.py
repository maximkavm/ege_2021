quantity = 0
for i in range(2 * 10 ** 5, 3 * 10 ** 5):
    if i % 5 != 0 and i % 4 != 0 and i % 10 == 6:
        quantity += 1
        print (i)
print(quantity)