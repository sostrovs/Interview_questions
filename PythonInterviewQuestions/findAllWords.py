import pprint

def displayList(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


def generateMatrix():
    L = [
        ['c', 'a', 't'],
        ['k', 'o', 'r'],
        ['l', 'm', 'e'],
    ]
    return L


def getLetters(L):
    letters = {}
    for i in range(len(L)):
        for j in range(len(L[i])):
            letters[(i, j)] = L[i][j]

    return letters


def getWordDictionary():
    words = {'cat', 'car', 'tromb', 'lock', 'lot', 'come'}
    return words


def getDict(L, M):
    D = {}

    for k in L.keys():
        for i in range(k[0] - 1, k[0] + 2):
            for j in range(k[1] - 1, k[1] + 2):
                if (0 <= i < len(M)) and (0 <= j < len(M[0])):
                    if k != (i, j):
                        if k not in D:
                            D[k] = [(i, j)]
                        else:
                            D[k].append((i, j))
    return D


def BFS(D, W, M):
    B = [[x] for x in D.keys()]
    P = [B]
    words = []
    while len(P) < len(M) * len(M[0]):
        B = []
        for x in P[-1]:
            for y in D[x[-1]]:
                if y not in x:
                    x_copy = x.copy()
                    x_copy.append(y)
                    B.append(x_copy)
                    word = "".join([M[a[0]][a[1]] for a in x_copy])
                    if word in W:
                        words.append(word)
        P.append(B)
    return P, words


def main():
    M = generateMatrix()
    W = getWordDictionary()
    L = getLetters(M)
    D = getDict(L, M)
    P, words = BFS(D, W, M)
    print(words)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(P)


if __name__ == '__main__':
    main()
