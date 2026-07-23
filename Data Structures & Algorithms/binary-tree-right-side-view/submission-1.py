# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        this_level_node = root.val
        result.append(this_level_node)
        while queue:
            lq = len(queue)
            for _ in range(lq):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    this_level_node = node.left.val
                if node.right:
                    queue.append(node.right)
                    this_level_node = node.right.val
            result.append(this_level_node)
        del result[-1]
        return result
                        

