f = open('27B-2-2.txt')
n = int(f.readline())
m10 = 0
m2 = 0
m5 = 0
m = 0
for i in range(n):
    x = int(f.readline())
    if x % 10 == 0 and x > m10:
        if m10 > m:
            m = m10 
        m10 = x
    elif x > m:
        m = x
    if x % 2 == 0 and x % 10 != 0 and x > m2:
        m2 = x
    if x % 5 == 0 and x % 10 != 0 and x > m5:
        m5 = x
print(m * m10)
print(m2 * m5)

