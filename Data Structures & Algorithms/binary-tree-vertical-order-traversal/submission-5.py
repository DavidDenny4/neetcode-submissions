# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        index_list = defaultdict(list)
        visited = set()
        res = []
    
        def dfs(node, index):
            if not node or node in visited:
                return

            visited.add(node)
            index_list[index].append(node.val)
            dfs(node.left, index - 1)
            dfs(node.right, index + 1)

        dfs(root, 0)
        min_index = min(index_list.keys())
        print(f"min index is {min_index}")
        for i in index_list:
            print(f"the key val is {i}")
            res.append(index_list[i])
        
        return res