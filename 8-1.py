import itertools

counter = 0
for i in itertools.product('БАЛКОН', repeat=5):
    if i.count('Б') >= 1:
        counter += 1

print(counter)

counter = 0
for i1 in 'БАЛКОН':
    for i2 in 'БАЛКОН':
        for i3 in 'БАЛКОН':
            for i4 in 'БАЛКОН':
                for i5 in 'БАЛКОН':
                    word = i1 + i2 + i3 + i4 + i5
                    if word.count('Б') >= 1:
                        counter += 1

print(counter)