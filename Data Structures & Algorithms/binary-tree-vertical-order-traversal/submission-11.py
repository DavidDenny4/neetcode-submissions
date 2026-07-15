# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        index = 0
        map = defaultdict(list)
        queue = deque()
        queue.append((root, index))

        while queue:
            for i in range(len(queue)):
                node, index = queue.popleft()
                map[index].append(node.val)
                if node.left:
                    queue.append((node.left, index - 1))
                if node.right:
                    queue.append((node.right, index + 1))
        
        min_index = min(map.keys())
        max_index = max(map.keys())
        res = []
        for i in range(min_index, max_index + 1):
            res.append(map[i])