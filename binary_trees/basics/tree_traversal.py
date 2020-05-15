# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):
    if root:
        print('preorder : ' + root.data)
        tree_traversal(root.left)

        print('inorder : ' + root.data)
        tree_traversal(root.right)

        print('postorder : ' + root.data)


""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""


# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

        # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        d_left = maxDepth(root.left)
        d_right = maxDepth(root.right)

        if d_left > d_right:
            return d_left + 1
        else:
            return d_right + 1


def main():
    H = TreeNode("H")
    G = TreeNode("G", H)
    F = TreeNode("F", None, G)
    D = TreeNode("D")
    E = TreeNode("E")
    C = TreeNode("C", D, E)
    B = TreeNode("B", C, F)

    M = TreeNode("M")
    L = TreeNode("L", None, M)
    N = TreeNode("N")
    K = TreeNode("K", L, N)
    P = TreeNode("P")
    O = TreeNode("O", None, P)
    J = TreeNode("J", None, K)
    I = TreeNode("I", J, O)

    A = TreeNode("A", B, I)

    tree_traversal(A)
    #printLevelOrder(A)
    #print(maxDepth(A))


if __name__ == "__main__":
    #main()

    stack = []

    stack.append((5,5))
    stack.append("c")
    print(stack)
