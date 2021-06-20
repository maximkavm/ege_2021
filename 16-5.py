cnt = 0
def F(n):
    global cnt
    cnt += n + 1
    if n > 1:
        cnt += n + 5
        F(n-1)
        F(n-2)
F(24)
print(cnt)