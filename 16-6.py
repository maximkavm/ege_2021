cache = {}
def f(n) :
    if n not in cache:
        if n == 1: cache[1] = 1
        if n > 1: cache [n] = n*f (n-1)
    return cache [n]
for i in range (1,3000) :
    f(i)

print(f(2023) / f(2020))