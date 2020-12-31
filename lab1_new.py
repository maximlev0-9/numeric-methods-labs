k = 11
s = 0.02 * k

A = [
    [8.3, 2.62 + s, 4.1, 1.9],
    [3.92, 8.45, 7.78 - s, 2.46],
    [3.77, 7.21 + s, 8.04, 2.28],
    [2.21, 3.65 - s, 1.69, 6.69]
]

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

# з вибором головного елемента по рядку
for b in range(n):
    # метод Гауса
    inx = []
    P = []

    for i in range(n):
        inx.append(i)

    for i in range(n):
        for j in range(n):
            V[i][j] = (A[i][j])
        P.append(E[i][b])

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

    # for i in range(n):
    #     X[i] = Y[i]
    #
    # X[n-1] = Y[n-1]

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

    for i in range(n):
        INVERS[i][b] = X[i]

print("Inversed matrix:")
for i in range(n):
    for j in range(n):
        print(round(INVERS[i][j], 4), end=' ')
    print()

check_matrix = [[], [], [], []]
for i in range(n):
    for j in range(n):
        check_matrix[i].append(0)

for i in range(n):
    for j in range(n):
        for k in range(n):
            check_matrix[i][j] += A[i][k] * INVERS[k][j]

print("Checked matrix:")
for i in range(n):
    for j in range(n):
        print(round(check_matrix[i][j], 4), end=' ')
    print()


# # з вибором головного елемента по всій матриці (відрізняється тільки частиною, де сортування)
# for i in range(n):
#     for j in range(n):
#         C[i][j] = 0
#         INVERS[i][j] = 0.0
#         if i == j:
#             E[i][j] = 1

# for b in range(n):
#     # метод Гауса
#     inx = []
#     P = []

#     for i in range(n):
#         inx.append(i)

#     for i in range(n):
#         for j in range(n):
#             V[i][j] = (A[i][j])
#         P.append(E[i][b])

#     for k in range(n):
#         # сортування
#         max_sth = abs(V[k][k])
#         w = k
#         h = k
#         for l in range(k, n):
#             for f in range(k, n):
#                 if max_sth < abs(V[l][f]):
#                     max_sth = abs(V[l][f])
#                     h = l
#                     w = f

#         value = P[k]
#         P[k] = P[h]
#         P[h] = value

#         for d in range(n):
#             value = V[k][d]
#             V[k][d] = V[h][d]
#             V[h][d] = value

#         z = inx[k]
#         inx[k] = inx[w]
#         inx[w] = z

#         for d in range(n):
#             if d < k:
#                 value = C[d][k]
#                 C[d][k] = C[d][w]
#                 C[d][w] = value
#             else:
#                 value = V[d][k]
#                 V[d][k] = V[d][w]
#                 V[d][w] = value
#         # кінець сортування

#         Y[k] = P[k] / V[k][k]
#         for i in range(k + 1, n):
#             P[i] -= V[i][k] * Y[k]
#             for j in range(k + 1, n):
#                 C[k][j] = V[k][j] / V[k][k]
#                 V[i][j] -= V[i][k] * C[k][j]

#         # for i in range(n):
#         #     X[i] = Y[i]
#         #
#         # X[n-1] = Y[n-1]

#     for i in range(n - 1, -1, -1):
#         X[i] = Y[i]
#         for j in range(i + 1, n):
#             X[i] -= C[i][j] * X[j]

#     for i in range(n):
#         if inx[i] != i:
#             z = inx[i]
#             value = X[i]
#             X[i] = X[z]
#             X[z] = value
#             inx[i] = inx[z]
#             inx[z] = z
#     # кінець методу Гауса

#     for i in range(n):
#         INVERS[i][b] = X[i]

# print("Inversed matrix:")
# for i in range(n):
#     for j in range(n):
#         print(round(INVERS[i][j], 4), end=' ')
#     print()

# check_matrix = [[], [], [], []]
# for i in range(n):
#     for j in range(n):
#         check_matrix[i].append(0)

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             check_matrix[i][j] += A[i][k] * INVERS[k][j]

# print("Checked matrix:")
# for i in range(n):
#     for j in range(n):
#         print(round(check_matrix[i][j], 4), end=' ')
#     print()
