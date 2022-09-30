# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist_head = ListNode()
        newlist = newlist_head
        
        while True:
            if list1 is None:
                newlist.next = list2
                break
                
            if list2 is None:
                newlist.next = list1
                break
            
            if list1.val < list2.val:
                newlist.next = list1
                list1 = list1.next
            else:
                newlist.next = list2
                list2= list2.next
                
            newlist = newlist.next
            
        return newlist_head.next