# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
                
        
        prev=None
        cur=slow
       
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        first=head
        second=prev
        
        while second:
            if second.val!=first.val:
                return False
            first=first.next
            second=second.next
        return True
            



            




        