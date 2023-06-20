for i in range(700001, 800000):
    b_delit = 0
    m_delit = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            b_delit = i // j
            m_delit = j
            break

    summ = b_delit + m_delit
    if summ % 10 == 8:
        print(i, summ)