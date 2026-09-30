# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(index):
            if not index:
                return 
                
            if index.left:
                helper(index.left)
            res.append(index.val)
            if index.right:
                helper(index.right)


        helper(root)
        return res