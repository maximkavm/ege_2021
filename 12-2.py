s = '1' * 2018 + '3' * 2050

while '111' in s:
    if '111' in s:
        s = s.replace('111', '2', 1)
    elif '222' in s:
        s = s.replace('222', '3', 1)
    elif '333' in s:
        s = s.replace('333', '1', 1)
print(s)

