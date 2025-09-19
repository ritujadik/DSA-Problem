class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    if not  root:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))