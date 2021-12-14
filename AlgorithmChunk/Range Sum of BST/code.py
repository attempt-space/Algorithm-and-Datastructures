# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
 

class Solution:
    def __init__(self):
        self.sum =0 
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if root is None:
            return
        
        if root.val >= low and root.val <= high:
            self.sum = self.sum+root.val
        
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)
        
        return self.sum
        
            