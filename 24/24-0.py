file = open('24.txt')
str = file.readline()
dict = dict()
for i in range(1, len(s)):
    if str[i-1] == 'A':
        dict[str[i]] = dict.get(str[i], 0) + 1
print(dict)