# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.hash = set()
        def bst(root):
            if root:
                if root.val in self.hash:
                    return True
                self.hash.add(k-root.val)
                return bst(root.left) or bst(root.right)
                
            return False
        return bst(root)
                
                
    