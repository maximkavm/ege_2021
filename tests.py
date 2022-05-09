# На числовой прямой даны два отрезка: D = [17; 58] и C = [29; 80].
# Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
# (x ∈ D) → ((¬(x ∈ C) /\ ¬(x ∈ A)) → ¬(x ∈ D)) истинно для всех x

for D in range(17, 58 + 1):
    print("passing", D)
    for C in range(29, 80 + 1):
        for A in range(1, 100):
            flag = True
            for x in range(1, 100):
                F1 = x in range(17, 58 + 1)
                F2 = not(x in range(29, 80 + 1))
                F3 = not(x in range(1, 100))
                F4 = not(x in range(17, 58 + 1))
                F = F1 <= ((F2 + F3) <= F4)
                if F == False:
                    flag = False
            if flag == True:
                print(A)
                break