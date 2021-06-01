f = open('24.txt')
s = f.readline()
cnt = 1
max_cnt = 1
for i in range(1, len(s)):
    if s[i:i+3] == 'XYZ':
        cnt += 3
        max_cnt = max(cnt, max_cnt)
    else:
        cnt = 1
print(max_cnt)