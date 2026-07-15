# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []

        def dfs(node):
            if not node:
                self.res.append("N")
            
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        print(f"res is {res}")
        
        return 
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        return