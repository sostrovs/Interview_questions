def getDictionary(L):
    D = {}
    for i in range(len(L) - 1):
        for j in range(len(L[i])):
            D[L[i][j]] = L[i + 1]

    return D


def getSets(D, cur, A, P):
    if cur not in D:
        A.append(cur)
        P.append(A)
    else:
        A.append(cur)
        for i in range(len(D[cur])):
            A_copy = A.copy()
            getSets(D, D[cur][i], A_copy, P)


def findAllSets(D, L):
    P = []
    for i in range(len(L[0])):
        getSets(D, L[0][i], [], P)

    return P


def main():
    L = [
        [1, 2, 3],
        ['a', 'b', 'c'],
        ['True', 'False']
    ]

    D = getDictionary(L)
    print(D)
    P = findAllSets(D, L)
    print(len(P), P)


if __name__ == '__main__':
    main()
