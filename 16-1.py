def f(n):
    if n <= 15:
        return n*n + 3*n + 9
    if n > 15 and n % 3 == 0:
        return f(n-1) + n - 2
    if n > 15 and n % 3 != 0:
        return f(n-2) + n + 2

def all_even(n):
    isEven = True
    while n > 0:
        if (n % 10) % 2 != 0:
            isEven = False
        n = n // 10
    return isEven

cnt = 0
for i in range(1, 1001):
    print(f(i))
    if all_even(f(i)):
        cnt+=1
print(cnt)