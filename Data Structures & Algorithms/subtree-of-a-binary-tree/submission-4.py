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
        
        if subRoot.val > root.val:
            return self.isSubtree(root.right, subRoot)
        elif subRoot.val < root.val:
            return self.isSubtree(root.left, subRoot)
        return root.val == subRoot.val