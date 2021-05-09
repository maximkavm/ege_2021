def f(n):
    if n <= 5:
        return n + 15 
    if n > 5 and n % 2 == 0:
        return f(n//2) + n*n*n - 1
    if n > 5 and n % 2 == 1:
        return f(n-1) + 2*n*n + 1
 
cnt = 0
for i in range(1, 1000):
    s = str(f(i))
    if s.count('8') >= 2:
        print(s)
        cnt+=1
print(cnt)