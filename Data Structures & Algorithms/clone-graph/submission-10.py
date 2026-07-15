"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clone = {}
        
        def dfs(n):
            if n not in clone:
                newNode = Node(n.val)
                clone[n] = newNode
                for neighbor in n.neighbors:
                    newNode.neighbors.append(dfs(neighbor))
            return clone[n]
        
        return dfs(node)
        # if node:
        #     return dfs(node)
        # else:
        #     return None
        
    