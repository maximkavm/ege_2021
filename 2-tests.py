print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = (not(x) or y or z) and (not(x) or not(z))
            if F == False:
                print(x,y,z)