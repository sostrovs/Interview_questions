class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right is not None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.val)

        # Print left branch
        if self.left is not None:
            ret += self.left.__str__(depth + 1)

        return ret


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def treeLength(root):
    if root is None:
        return 0
    else:
        return max(treeLength(root.left), treeLength(root.right)) + 1


def main():
    L = [50, 30, 20, 40, 70, 60, 80, 45, 55, 65, 66, 67, 68]
    r = Node(L[0])
    for i in range(1, len(L)):
        insert(r, Node(L[i]))

    print(r.__str__())
    print(treeLength(r))


if __name__ == '__main__':
    main()
