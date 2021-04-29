print ('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                ###
                F = ((x & (y | (not z)) & w) == (x <= ((not y) & z)))
                ###
                if F == True:
                    print(w, x, y, z)
