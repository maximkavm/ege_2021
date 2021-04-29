def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 

    return s

def change(n):

    s = decto(n, 2)
    s = s + s[-2]
    s = s + s[1]
    n = int(s, base=2)
    return n

# print(s)
# print(change(n))

for i in range(2, 1000):
    if change(i) <= 190:
        print(i)