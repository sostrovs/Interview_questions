class Node:
    def __init__(self, val, parent=None):
        self.parent = parent
        self.val = val

def findCommonAncestor(node1, node2):
    nodes = set([])
    while node1 is not None:
        nodes.add(node1.val)
        node1 = node1.parent

    while node2 is not None:
        if node2.val in nodes:
            return node2.val
        else:
            node2 = node2.parent

    return None


def main():
    L = [50, 30, 20, 40, 70, 60, 80, 45, 55, 65, 66, 67, 68]
    n50 = Node(50)
    n30 = Node(30, n50)
    n20 = Node(20, n30)
    n40 = Node(40, n30)
    n70 = Node(70, n50)
    n60 = Node(60, n70)
    n80 = Node(80, n70)
    n45 = Node(45, n40)
    n55 = Node(55, n60)
    n65 = Node(65, n60)
    n66 = Node(66, n65)
    n67 = Node(67, n66)
    n68 = Node(68, n67)

    print(findCommonAncestor(n20, n68))


if __name__ == '__main__':
    main()