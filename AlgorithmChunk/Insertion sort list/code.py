# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def sortedlist(self,sort,newnode):
        
        current = None
        if ((sort == None) or sort.val >= newnode.val):
            newnode.next = sort
            sort = newnode
            
        else:
            current= sort
            while (current.next != None and (current.next.val < newnode.val)):
                current = current.next
            
            newnode.next = current.next
            current.next = newnode
            
        return sort

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = None
        current = head
        
        while (current !=None):
            next = current.next
            sorted_list = self.sortedlist(sorted_list,current)    
            
            current = next
        head = sorted_list
        return head
            
            
            
            
            