def isPalindrome(S):
    for i in range(int(len(S) / 2)):
        if S[i] != S[-1 - i]:
            return False

    return True


def buildPalidrome(S):
    np_str = ""
    for i in range(len(S)):
        if isPalindrome(S[i:len(S)]):
            return S[0:len(S)] + np_str
        else:
            np_str = str(S[i]) + np_str


def main():
    print(buildPalidrome("sergey"))
    print(buildPalidrome("sara"))
    print(buildPalidrome("saras"))


if __name__ == '__main__':
    main()
