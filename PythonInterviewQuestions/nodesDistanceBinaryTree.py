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


def nodeDistance(node, val):
    length = 0

    while node is not None:
        if node.val == val:
            return length
        else:
            length += 1
            if node.val > val:
                node = node.left
            else:
                node = node.right

    return -1


def findNodeDistance(root, node1, node2):
    if node1 > node2:
        node1, node2 = node2, node1

    while root is not None:
        if (node1 <= root.val <= node2):
            length_n1 = nodeDistance(root, node1)
            length_n2 = nodeDistance(root, node2)
            if length_n1 > -1 and length_n2 > -1:
                return length_n1 + length_n2
            else:
                return -1
        else:
            if node1 < root.val and node2 < root.val:
                root = root.left
            else:
                root = root.right


def main():
    L = [50, 30, 20, 40, 70, 60, 80, 45, 55, 65, 66, 67, 68]
    r = Node(L[0])
    for i in range(1, len(L)):
        insert(r, Node(L[i]))

    print(r.__str__())
    print(findNodeDistance(r, 45, 68))


if __name__ == '__main__':
    main()
