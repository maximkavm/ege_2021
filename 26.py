f=open('tests.txt')

s=f.readline().split()
n=int(s[0])
m=int(s[1])

X, Y, Z = [], [], []

for i in range(n):
    s=f.readline().split()
    X.append((int(s[0]), s[1]))

X.sort()
print(X)
sm=0

for i in range(n):
    if sm+X[i][0]<= m:
        sm=sm+X[i][0]
        Y.append(X[i])
    else:
        if X[i][1]=='A':
            Z.append(X[i])


j=0
for i in range(len(Y)-1, -1, -1):

    if Y[i][1]=='A': continue
    
    if sm - Y[i][0] + Z[j][0] <= m:
        sm = sm - Y[i][0] + Z[j][0]
        Y[i] = Z[j]
    else:
        break

    j=j+1

count = 0
for i in range(len(Y)):
    if Y[i][1]=='A':
        count=count+1

print(count, m-sm)