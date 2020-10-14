def bubbleSort(L):
    for i in range(len(L) - 1):
        done = True
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                done = False
        if done:
            break


def main():
    L = [5, 2, 6, 4, 7, 8, 1, 10, 14, 23, 54, 33]
    print(L)
    bubbleSort(L)
    print(L)


if __name__ == '__main__':
    main()
