def genarateZeroMatrix(n, m):
    A = [[0 for x in range(n)] for x in range(m)]
    return A


def displayList(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


def numberOfPaths(n, m):
    A = genarateZeroMatrix(n, m)
    for i in range(m):
        for j in range(n):
            if not (i == 0 and j == 0):
                if (i == 0 and j != 0) or (i != 0 and j == 0):
                    A[i][j] = 1
                else:
                    A[i][j] = A[i - 1][j] + A[i][j - 1]

    return A


def main():
    L = numberOfPaths(4, 5)
    displayList(L)


if __name__ == '__main__':
    main()
