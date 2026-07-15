# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root.val


        def checkIn(root, p) -> bool:
            if not root:
                return False
            
            if root.val == p.val or checkIn(root.left, p) or checkIn (root.right, p):
                return True
            return False

        queue = deque()
        queue.append(root)
        while(len(queue) > 0):
            for i in range(len(queue)):
                node = queue.popleft()
                if checkIn(node, p) and checkIn(node, q):
                    lca = node.val
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(ndoe.right)
        return lca
        