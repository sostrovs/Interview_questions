def getList(elem):
    s = {str, int, float, bool, type(None)}
    if type(elem) in s:
        return [elem]
    else:
        L = []
        if type(elem) == dict:
            for i in elem:
                L.extend(getList(i))
                L.extend(getList(elem[i]))
        else:
            for i in elem:
                L.extend(getList(i))

        return L


def main():
    D = [1, 3, 4, ['a', 'b', (5, 6, 7), {'d': {'p': [33, 44, None]}}],
         {True, False, (None, True, 'b')}]
    print(D)
    print(getList(D))


if __name__ == '__main__':
    main()
