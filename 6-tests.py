count = 0
digits = set('01234567')
for x1 in digits:
    for x2 in digits:
        for x3 in digits:
            for x4 in digits:
                for x5 in digits:
                    f = x1 + x2 + x3 + x4 + x5
                    if f.count('6') == 1 and x1 != '0':
                        uneven = set('1357')
                        if x1 == '6':
                            if x2 not in uneven:
                                count += 1
                        elif x2 == '6':
                            if x1 not in uneven and x3 not in uneven:
                                count += 1
                        elif x3 == '6':
                            if x2 not in uneven and x4 not in uneven:
                                count += 1
                        elif x4 == '6':
                            if x5 not in uneven and x3 not in uneven:
                                count += 1
                        elif x5 == '6':
                            if x4 not in uneven:
                                count += 1
print(count)