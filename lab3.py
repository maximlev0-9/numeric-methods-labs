f_func = [
    lambda x_1, x_2: x_1 ** 2 + x_2 ** 2 + 0.1 - x_1,
    lambda x_1, x_2: 2 * x_1 * x_2 + 0.1 - x_2
]

f_x_func = [
    [
        lambda x_1, x_2: 2 * x_1 - 1,
        lambda x_1, x_2: 2 * x_2
    ],
    [
        lambda x_1, x_2: 2 * x_2,
        lambda x_1, x_2: 2 * x_1 - 1
    ]
]

n = 2
E = [
    [0.0, 0.0],
    [0.0, 0.0]
]
V = [
    [0.0, 0.0],
    [0.0, 0.0]
]
C = [
    [0.0, 0.0],
    [0.0, 0.0]
]

Y = [0.0, 0.0]
X = [0.0, 0.0]

INVERS = [
    [0.0, 0.0],
    [0.0, 0.0]
]

e = 0.00001

f_values = [0, 0]
J = [[0, 0], [0, 0]]

x = [0.0, 0.0]
x_old = [0.0, 0.0]


def is_not_ok():
    is_Ok = True
    # print(x)
    # print(x_old)
    for i in range(n):
        is_Ok = is_Ok and abs((x[i] - x_old[i]) / x[i]) < e
        x_old[i] = x[i]

    for i in range(n):
        pass
    return is_Ok


def main():
    counter = 0
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            INVERS[i][j] = 0.0
            if i == j:
                E[i][j] = 1

    while True:
        counter += 1
        for i in range(n):
            f_values[i] = f_func[i](x[0], x[1])
            for j in range(n):
                J[i][j] = f_x_func[i][j](x[0], x[1])

        for b in range(n):
            # метод Гауса
            inx = []
            P = []

            for i in range(n):
                inx.append(i)

            for i in range(n):
                for j in range(n):
                    V[i][j] = (J[i][j])
                P.append(E[i][b])

            for k in range(n):
                # сортування
                max_sth = abs(V[k][k])
                w = k
                h = k
                for l in range(k, n):
                    for f in range(k, n):
                        if max_sth < abs(V[l][f]):
                            max_sth = abs(V[l][f])
                            h = l
                            w = f

                value = P[k]
                P[k] = P[h]
                P[h] = value

                for d in range(n):
                    value = V[k][d]
                    V[k][d] = V[h][d]
                    V[h][d] = value

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

            for i in range(n):
                INVERS[i][b] = X[i]

        for i in range(n):
            for j in range(n):
                x[i] = x[i] - INVERS[i][j] * f_values[j]

        if is_not_ok():
            break
    return counter


print("count: ", main())
print(x)

for i in range(n):
    print(f_func[i](x[0],x[1]))
