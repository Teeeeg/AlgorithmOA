def are_identical(root1, root2):
    return recursiveCore(root1, root2)


def recursiveCore(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and root2:
        return root1.data == root2.data and recursiveCore(root1.left, root2.left) and recursiveCore(root1.right, root2.right)

    return False
