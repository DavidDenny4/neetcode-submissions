# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        result.append(self.inorderTraversal(root.left).val)
        result.append(root.val)
        result.append(self.inorderTraversal(root.right).val)
        return result