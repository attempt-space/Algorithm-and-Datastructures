# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def solve(self,root,arr):
        if root == None: 
            return
        arr.append(root.val)
        for i in (root.children):
            self.solve(i,arr)
                
    def preorder(self, root: 'Node') -> List[int]:
        arr=[]
        self.solve(root,arr)
        return arr
        

            