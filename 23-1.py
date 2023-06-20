for n in range(999, 100000000):
    number = str(n)
    nechet = 0
    summ = 0
    for i in range(len(number)):
        if (i + 1) % 2 == 1:
            nechet += int(number[i])
        summ += int(number[i])
    if abs(summ - nechet) == 29:
        print(n)
        break