words = 0
for i in 'ЛЕТО':
    for i2 in 'ЛЕТО':
        for i3 in 'ЛЕТО':
            for i4 in 'ЛЕТО':
                for i5 in 'ЛЕТО':
                    s = i + i2 + i3 + i4 + i5
                    if s.count('Е') >= 1:
                       words += 1
print(words)