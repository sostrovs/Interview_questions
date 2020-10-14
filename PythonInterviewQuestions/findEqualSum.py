def getEqualSum(L, first, last, M):
    mid = int((first + last) / 2)
    if mid in M:
        mid += 1
        if mid in M:
            mid -= 2
            if mid in M:
                return "No equal sum"

    M.add(mid)

    if sum(L[0:mid + 1]) == sum(L[mid + 1:]):
        return mid
    else:
        if sum(L[0:mid + 1]) < sum(L[mid + 1:]):
            return getEqualSum(L, mid + 1, len(L) - 1, M)
        else:
            return getEqualSum(L, 0, mid, M)


def findEqualSum(L):
    return getEqualSum(L, 0, len(L) - 1, set([]))


def main():
    # L = [5, 8, 9, 3, 3, 3, 4, 4, 5]
    L = [1, 5, 8, 9, 1, 3, 3, 3, 4, 4, 5, 2]
    print(findEqualSum(L))


if __name__ == '__main__':
    main()
