# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = 0

        def helper(node):
            if not node:
                return 0
            
            height = 1 + max(helper(node.left), helper(node.right))
            return height
        
        return helper(root)