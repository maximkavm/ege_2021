print ('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                ###
                F = (x == (not z)) <= ((x or w) == y)
                ###
                if F == False:
                    print(w, x, y, z)
