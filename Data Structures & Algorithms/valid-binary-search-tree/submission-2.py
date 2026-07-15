# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        if not root.left and not root.right:
            return True
        if root.left and (root.left.val > root.val or self.isValidBST(root.left) is False):
            return False
        if root.right and (root.right.val < root.val or self.isValidBST(root.right) is False):
            return False
        
        return True