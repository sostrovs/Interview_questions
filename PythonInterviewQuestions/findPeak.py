def getPeak(L, first, last):
    mid = int((first + last) / 2)
    if L[first] <= L[mid] <= L[last]:
        return last

    if L[first] >= L[mid] >= L[last]:
        return first

    left = getPeak(L, first, mid-1)
    right = getPeak(L, mid+1, last)
    if L[left] <= L[mid] <= L[right]:
        return right

    if L[left] >= L[mid] >= L[right]:
        return left

    return mid


def findPeak(L):
    return getPeak(L, 0, len(L) - 1)


def main():
    L = [1, 2, 5, 6, 7, 8, 25, 13, 11, 1]
    print(L)
    print(findPeak(L))


if __name__ == '__main__':
    main()
