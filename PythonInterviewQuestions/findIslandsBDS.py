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


def BFS(L, x, y, val, visited):
    A = [(x, y)]
    visited.append((x, y))
    queue = [(x, y)]
    while len(queue) > 0:
        next = []
        x, y = queue.pop(0)
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (0 <= i < len(L)) and (0 <= j < len(L[0])):
                    if L[i][j] == val and (i, j) not in visited:
                        A.append((i, j))
                        visited.append((i, j))
                        next.append((i, j))
        queue.extend(next)

    return A

def main():
    L = generateMatrix()
    displayList(L)
    visited, B = [], []
    for i in range(len(L)):
        for j in range(len(L[0])):
            if (i, j) not in visited:
                A = BFS(L, i, j, L[i][j], visited)
                B.append(A)

    for b in B:
        print(b)


if __name__ == '__main__':
    main()
