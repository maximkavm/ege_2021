def f(n):
    if n < 2:
        return n 
    if n >= 2 and n % 2 == 0:
        return n / 2 + 1
    if n >= 2 and n % 2 == 1:
        return 3 * n + 1

cnt = 0
for i in range(1, 101):
    if f(i) > 100:
        cnt+=1
print(cnt)