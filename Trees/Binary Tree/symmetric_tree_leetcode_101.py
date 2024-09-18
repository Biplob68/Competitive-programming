class TreeNode:
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symmetric(root):
    if root is None:
        return True
    return check_symmetric(root.left, root.right)


def check_symmetric(p, q):
    if not p or not q:
        return p == q

    elif p.val != q.val:
        return False
    return check_symmetric(p.left, q.right) and check_symmetric(p.right, q.left)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)

    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)

    p.right.left = TreeNode(4)
    p.right.right = TreeNode(3)

    print(is_symmetric(p))
