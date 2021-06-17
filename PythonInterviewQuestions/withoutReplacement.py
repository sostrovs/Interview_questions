def withoutR(A):
    W = []
    for i in range(len(A)):
        for j in range(len(A)):
            B = A.copy()
            for k in range(j, len(A)):
                B[k] = A[i]
                if B not in W:
                    W.append(B.copy())
                    L = B.copy()
                    for m in range(len(L)):
                        for n in range(len(L) - 1):
                            if L not in W:
                                W.append(L.copy())
                            L[n], L[n + 1] = L[n + 1], L[n]

    return W


def main():
    data = ['ab', 'baa', 'ca']
    result = withoutR(data)
    print(result, len(result))


if __name__ == '__main__':
    main()
