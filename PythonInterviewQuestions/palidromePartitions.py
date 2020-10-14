def isPalindrome(S):
    for i in range(int(len(S) / 2)):
        if S[i] != S[-1 - i]:
            return False

    return True


def getPalidromes(S):
    D = {}
    for i in range(len(S)):
        for j in range(i, len(S)):
            if isPalindrome(S[i:j + 1]):
                if i in D:
                    D[i].append(S[i:j + 1])
                else:
                    D[i] = [S[i:j + 1]]

    return D


def getPartitions(D, cur, P, L):
    if cur >= len(D):
        L.append(P)
    else:
        for i in range(len(D[cur])):
            P_new = P.copy()
            P_new.append(D[cur][i])
            cur_new = cur + len(P_new[-1])
            getPartitions(D, cur_new, P_new, L)


def findPalidromePartitions(S):
    D = getPalidromes(S)
    L = []
    getPartitions(D, 0, [], L)
    print(D)
    return L


def main():
    print(findPalidromePartitions("aabaa"))


if __name__ == '__main__':
    main()
