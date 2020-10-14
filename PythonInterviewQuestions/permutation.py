def getPermutationSets(S):
    L = list(S)
    P = []
    for i in range(len(L)):
        for j in range(len(L) - 1):
            P.append("".join(L))
            L[j], L[j + 1] = L[j + 1], L[j]

    return P


def main():
    print(getPermutationSets("abc"))


if __name__ == '__main__':
    main()
