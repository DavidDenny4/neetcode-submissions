# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            print(f"value of current node is {node.val}")
            left_edges = dfs(node.left)
            right_edges = dfs(node.right)
            print(f"{left_edges} _ {right_edges}")
            self.diameter = max(self.diameter, left_edges + right_edges)
            print(f"{node.val} has diameter of ")
            return 1 + max(left_edges, right_edges)
        
        return self.diameter