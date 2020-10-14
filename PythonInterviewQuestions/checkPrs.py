def checkPrs(mystr):
    s = set(["(", "[", "{"])
    d = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in mystr:
        if c in s:
            stack.append(c)
            continue

        if c in d:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0


def main():
    print(checkPrs("((())"))
    print(checkPrs("((()))"))
    print(checkPrs("[((()))]"))
    print(checkPrs("}((())"))


if __name__ == '__main__':
    main()
