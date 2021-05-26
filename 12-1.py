s = 20 * [3] + 22 * [4] + 10 * [5]

while s.max > 1 or s.max > 2 or s.max > 3:
    if s.max > 3:
        s = s.replace('10', '0001', 1)

while '1' in s or '10' in s:
    if '10' in s:
        s = s.replace('10', '0001', 1)
    else:
        s = s.replace('1', '000', 1)
print(s.count('0'))