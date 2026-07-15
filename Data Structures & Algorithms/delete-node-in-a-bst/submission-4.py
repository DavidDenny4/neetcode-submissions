# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left != None:
            return self.findMin(root.left)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if key < root.val:
            self.deleteNode(root.left, key)
        elif key > root.val:
            self.deleteNode(root.right, key)
        elif key == root.val:
            # find the min leaf from right child
            min_node = self.findMin(root)
            min_node.right = root.right
            min_node.left = root.left
            root = min_node
            self.deleteNode(min_node, min_node.val)
        return root    

