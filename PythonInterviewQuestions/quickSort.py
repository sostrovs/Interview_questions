def quickSort(L, first, last):
    if first < last:
        splitPoint = partition(L, first, last)
        quickSort(L, first, splitPoint - 1)
        quickSort(L, splitPoint + 1, last)


def partition(L, first, last):
    pivotValue = L[last]
    i = first - 1
    for j in range(first, last + 1):
        if L[j] <= pivotValue:
            i += 1
            L[j], L[i] = L[i], L[j]

    return i


def main():
    L = [5, 2, 6, 4, 7, 8, 1, 10, 14, 23, 54, 33]
    print(L)
    quickSort(L, 0, len(L) - 1)
    print(L)


if __name__ == '__main__':
    main()
