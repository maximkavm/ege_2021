s = '5' + 152 * '6' + '5'

while '63' in s or '664' in s or '6665' in s:
    if '63' in s:
        s.replace('63', '4')
        print(s)
    elif '664' in s:
        s.replace('664', '65')
    elif '6665' in s:
        s.replace('6665', '663')
print(s)
