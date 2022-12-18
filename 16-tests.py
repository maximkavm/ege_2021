cache = [0, 1]

n = 2
for i in range(2, 2023 + 1):
    cache.append(cache[i - 1] * i)


print(cache[2023] / cache[2020])