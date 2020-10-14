def displayList(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


def generateList(n, length):
    L = []
    for i in range(1, n+1, length):
        A = []
        for j in range(5):
            A.append(i+j)
        L.append(A)

    return L


def getSpiralList(A):
    sr, er = 0, len(A)
    sc, ec = 0, len(A[0])
    L = []

    while sc < ec:
        for i in range(sc, ec):
            L.append(A[sr][i])
        sr += 1
        if sr == er:
            break

        for i in range(sr, er):
            L.append(A[i][ec-1])
        ec -= 1
        if sc == ec:
            break

        for i in range(ec-1, sc-1, -1):
            L.append(A[er-1][i])
        er -= 1
        if sr == er:
            break

        for i in range(er-1, sr-1, -1):
            L.append(A[i][sc])
        sc += 1

    return L


def main():
    L = generateList(25, 5)
    displayList(L)
    print(getSpiralList(L))


if __name__ == '__main__':
    main()
