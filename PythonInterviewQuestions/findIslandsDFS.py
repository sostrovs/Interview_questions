def displayList(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


def generateMatrix():
    L = [
        [1, 1, 2, 3, 3],
        [1, 1, 2, 3, 2],
        [1, 1, 2, 2, 2],
        [3, 3, 2, 2, 2],
        [1, 3, 1, 1, 1],
        [1, 1, 3, 2, 2]
    ]
    return L


def DFS(L, x, y, val, visited, A):
    if L[x][y] == val and (x, y) not in visited:
        A.append((x, y))
    visited.append((x, y))
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (0 <= i < len(L)) and (0 <= j < len(L[0])):
                if L[i][j] == val and (i, j) not in visited:
                    DFS(L, i, j, val, visited, A)


def main():
    L = generateMatrix()
    displayList(L)

    A, visited, B = [], [], []

    for i in range(len(L)):
        for j in range(len(L[0])):
            if (i, j) not in visited:
                DFS(L, i, j, L[i][j], visited, A)
                B.append(A)
                A = []

    for b in B:
        print(b)


if __name__ == '__main__':
    main()
