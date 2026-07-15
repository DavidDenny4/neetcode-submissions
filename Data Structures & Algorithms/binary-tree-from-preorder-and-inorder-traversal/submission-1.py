# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def insert(root, val):
            if not root:
                return TreeNode(val)
            
            if val > root.val:
                root.right = insert(root.right, val)
            if val < root.val:
                root.left = insert(root.left, val)
            return root

        root = TreeNode(inorder[0])
        for i in range(1, len(inorder)):
            insert(root, i)
        

        print(root.val)
        return

            