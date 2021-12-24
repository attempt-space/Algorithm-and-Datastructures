# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 
class Solution:
    
    def reverse(self,node):
        prevNode = node
        node = node.next
        currNode = node
        prevNode.next= None
        
        while node:
            node = node.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = node
        return prevNode
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or head.next == None:
            return
        
        slowPointer = head
        fastPointer = head.next
        while (fastPointer != None and fastPointer.next !=None):
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        node1 = head
        node2 = slowPointer.next
        slowPointer.next = None
        node2 = self.reverse(node2)
        
        node = ListNode()
        curr = node
        
        while (node1 != None or node2 !=None):
            if (node1 !=None):
                curr.next = node1
                curr= curr.next
                node1 = node1.next
                
            if (node2 !=None):
                curr.next = node2
                curr= curr.next
                node2 = node2.next
            
        node = node.next
