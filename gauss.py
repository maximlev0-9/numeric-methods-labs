def gaussFunc(A, B):
    n = 4
    E = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    V = [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0]
    ]
    C = [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0]
    ]

    Y = [0.0, 0.0, 0.0, 0.0]
    X = [0.0, 0.0, 0.0, 0.0]

    INVERS = [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0]
    ]

    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            INVERS[i][j] = 0.0
            if i == j:
                E[i][j] = 1

    # # з вибором головного елемента по рядку
    # for b in range(n):
        # метод Гауса
    inx = []
    P = B

    for i in range(n):
        inx.append(i)

    for i in range(n):
        for j in range(n):
            V[i][j] = (A[i][j])

    for k in range(n):
        # сортування
        max_sth = abs(V[k][k])
        w = k
        for l in range(k + 1, n):
            if max_sth < abs(V[k][l]):
                max_sth = abs(V[k][l])
                w = l
        z = inx[k]
        inx[k] = inx[w]
        inx[w] = z
        for d in range(n):
            if d < k:
                value = C[d][k]
                C[d][k] = C[d][w]
                C[d][w] = value
            else:
                value = V[d][k]
                V[d][k] = V[d][w]
                V[d][w] = value
        # кінець сортування

        Y[k] = P[k] / V[k][k]
        for i in range(k + 1, n):
            P[i] -= V[i][k] * Y[k]
            for j in range(k + 1, n):
                C[k][j] = V[k][j] / V[k][k]
                V[i][j] -= V[i][k] * C[k][j]


    for i in range(n - 1, -1, -1):
        X[i] = Y[i]
        for j in range(i + 1, n):
            X[i] -= C[i][j] * X[j]

    for i in range(n):
        if inx[i] != i:
            z = inx[i]
            value = X[i]
            X[i] = X[z]
            X[z] = value
            inx[i] = inx[z]
            inx[z] = z
        # кінець методу Гауса
    # print(X)
    return X