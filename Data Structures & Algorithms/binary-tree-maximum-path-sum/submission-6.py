# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.all_max = float("-inf")

        # return the max sum you can get from that node
        def dfs(node):

            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_max = node.val + max(left_sum, 0) + max(right_sum, 0)
            self.all_max = max(self.all_max, curr_max)
            best_path = max(left_sum, right_sum)
            return node.val + best_path if best_path > 0 else node.val

        dfs(root)
        return self.all_max





