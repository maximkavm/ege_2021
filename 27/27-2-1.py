f = open('27B-2-1.txt')
n = int(f.readline())
m13 = 0
m = 0
for i in range(n):
    x = int(f.readline())
    if x % 13 == 0 and x > m13:
        if m13 > m:
            m = m13 
        m13 = x
    elif x > m:
        m = x
print(m * m13)
