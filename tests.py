from math import ceil

file = open('tests.txt')

n = int(file.readline())
elements = []

for i in range(n):
    a, b = map(int, file.readline().split())
    elements.append([a, ceil(b / 36)])

cost = [0] * n
rightSum = 0
leftSum = 0

for i in range(1, n):
    cost[0] += (elements[i][0] - elements[0][0]) * elements[i][1]
    rightSum += elements[i][1]
    
print(cost)

for i in range(1, n):
    leftSum += elements[i - 1][1]
    cost[i] = cost[i - 1] - rightSum * (elements[i][0] - elements[i - 1][0]) + leftSum * (elements[i][0] - elements[i - 1][0])
    rightSum -= elements[i][1]

print(min(cost))