f = open('24.txt')
s = f.readline()
cnt = 0
max_cnt = 0
i = 0
while i < len(s):
    if s[i:i+3] == 'XYZ':
        cnt += 3
        max_cnt = max(cnt, max_cnt)
        i += 3
    elif s[i:i+2] == 'XY':
        cnt += 2
        max_cnt = max(cnt, max_cnt)
        i += 2
        cnt = 0
    elif s[i:i+1] == 'X':
        cnt += 1
        max_cnt = max(cnt, max_cnt)
        i += 1
        cnt = 0
    else:
        cnt = 0
        i += 1

print(max_cnt)