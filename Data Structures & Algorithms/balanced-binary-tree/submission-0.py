# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            return 1+ max(lh,rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (abs(self.height(root.left) - self.height(root.right))) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        