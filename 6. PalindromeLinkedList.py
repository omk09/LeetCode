# algorithm 
# if we read it from right to left or from left to right it must be the same 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
    
        def reverseLinkedList(head):
            previous = None 
            current = head 
            
            if head == None: 
                return head
            
            while current is not None: 
                next_node = current.next 
                current.next = previous
                previous = current 
                current = next_node
            return previous
    # begin 
        if head is None: return True 
        
        
    # Find the end of first half and reverse second half.
        fast = head 
        slow = head
        
        while(fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next 
        
        fast = head
        
        slow = reverseLinkedList(slow.next)
        
        while slow is not None:
            if fast.val != slow.val:
                return False 
            
            fast = fast.next
            slow = slow.next 
        return True
            