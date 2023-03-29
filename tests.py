file = open('tests.txt')
lines = file.readlines()

count = 0
mx = 0

numbers = []
for line in lines:
    numbers.append(int(line))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) % 9 == 0:
            count += 1
            mx = max(numbers[i]+numbers[j], mx)

print(count, mx)