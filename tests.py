def f(n):
    #print(2 * n)
    s = 2 * n
    if n > 1:
        #print(n - 5)
        s += n - 5
        #f(n - 1)
        #f(n - 2)
        return s + f(n-1) + f(n-2)
    return  s

n = 0
while True:
    n += 1
    s = f(n)
    if s > 500000:
        break
print(n, s)