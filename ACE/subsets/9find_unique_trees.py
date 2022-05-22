
from cProfile import run
from logging import root


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []

    return findUnique_trees_recursive(1, n)


def findUnique_trees_recursive(start, end):
    res = []
    if start > end:
        res.append(None)
        return res

    for i in range(start, end+1):
        leftSubtree = findUnique_trees_recursive(start, i-1)
        rightSubtree = findUnique_trees_recursive(i+1, end)
        for leftTree in leftSubtree:
            for rightTree in rightSubtree:
                root = TreeNode(i)
                root.left = leftSubtree
                root.right = rightSubtree
                res.append(root)
    return res


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
