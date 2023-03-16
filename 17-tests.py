numbers = []
for i in range(1012, 9368 + 1):
    if i % 3 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        numbers.append(i)

print(numbers)
print(len(numbers), max(numbers))
