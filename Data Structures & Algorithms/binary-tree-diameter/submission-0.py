# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root, diam):
        if not root:
            return 0
        else:
            left_h = self.height(root.left,diam)
            right_h = self.height(root.right,diam)
            diam[0] = max(diam[0], left_h + right_h)
            return 1 + max(left_h , right_h)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0] # this was missing
        self.height(root, diam)
        return diam[0]


        