from queue import Queue


class Node:
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    p1 = Queue()
    q1 = Queue()

    p1.put(p)
    q1.put(q)

    while not p1.empty() and not q1.empty():
        val1 = p1.get()
        val2 = q1.get()

        if val1.val != val2.val:
            return False
        if (val1.left and not val2.left) or (not val1.left and val2.left):
            return False
        if (val1.right and not val2.right) or (not val1.right and val2.right):
            return False
        
        if val1.left and val2.left:
            p1.put(val1.left)
            q1.put(val2.left)

        if val1.right and val2.right:
            p1.put(val1.right)
            q1.put(val2.right)

    return True


if __name__ == '__main__':
    p = Node(1)
    p.left = Node(2)
    p.right = Node(3)

    q = Node(1)
    q.left = Node(2)
    q.right = Node(3)
    print(is_same_tree(p, q))
    # p = [1, 2, 3]
    # q = [1, 2, 3]
    # print()
