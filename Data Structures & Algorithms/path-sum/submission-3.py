# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root.left and not root.right:
            if -root.val == targetSum:
                return True
            return False
        
        if root.left:
            return self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            return hasPathSum(root.right, targetSum - root.val)
        
        return False