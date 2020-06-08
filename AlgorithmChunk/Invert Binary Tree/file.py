

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        if not root:
            return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        if root.left and root.right == None:
            root.right = root.left
            root.left = None
            
        elif root.right and root.left == None:
            root.left = root.right     
            root.right = None
            
            
        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
        return root
        """
        # Simple & elegant one
        if root is None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
            
        
