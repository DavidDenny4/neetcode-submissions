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
                return 
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        self.index = 0
        vals = data.split(",")

        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            
            newNode = TreeNode(int(vals[self.index]))
            self.index += 1
            newNode.left = dfs()
            newNode.right = dfs()
            return newNode
            
        return dfs()







