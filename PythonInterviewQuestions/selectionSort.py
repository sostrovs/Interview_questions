def selectionSort(L):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]


def main():
    L = [5, 2, 6, 4, 7, 8, 1, 10, 14, 23, 54, 33]
    print(L)
    selectionSort(L)
    print(L)


if __name__ == '__main__':
    main()
