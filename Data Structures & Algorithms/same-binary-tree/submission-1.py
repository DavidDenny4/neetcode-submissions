# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q) or (p.val != q.val) or (self.isSameTree(p.left, q.left) is False) or (self.isSameTree(p.right, q.right) is False):
            return False
        return True

        