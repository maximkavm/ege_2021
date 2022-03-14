def makeMagic(first, second):
    senior = int(first[0]) + int(second[0])
    middle = int(first[1]) + int(second[1])
    junior = int(first[2]) + int(second[2])

    array = [senior, middle, junior].sort(reverse=True)

    s = str(array[0]) + str(array[1]) + str(array[2])
    return s

for i in range(100, 1000):
    if makeMagic("486", str(i)) == str(13107):
        print(i)
