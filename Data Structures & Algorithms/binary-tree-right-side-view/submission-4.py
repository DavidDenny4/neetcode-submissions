from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()

        if root:
            queue.append(root)
        
        while(len(queue) > 0):
            
            for i in range(len(queue)):

                node = queue.popleft()
                print(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                
                if i == 0:
                    print(f"only adding {node.val} to the result")
                    result.append(node.val)
                
            
        return result