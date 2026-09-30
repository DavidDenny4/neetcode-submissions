# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root == subRoot:
            return True
        if subRoot.val > root.val:
            return self.isSubtree(root.right, subRoot)
        if subRoot.val < root.val:
            return self.isSubtree(root.left, subRoot)
        return False